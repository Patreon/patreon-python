# api.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import requests
import six

from patreon.jsonapi.parser import JSONAPIParser
from patreon.jsonapi.url_util import build_url
from patreon.utils import user_agent_string
from patreon.version_compatibility.utc_timezone import utc_timezone
from six.moves.urllib.parse import urlparse, parse_qs, urlencode


class API(object):
    def __init__(self, access_token):
        super(API, self).__init__()
        self.access_token = access_token

    def get_campaigns(self, page_size, cursor=None,  includes=None, fields=None):
        url = 'campaigns'
        params = {'page[count]': page_size}
        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            params.update({'page[cursor]': cursor})
        url += "?" + urlencode(params)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    def get_identity(self, includes=None, fields=None):
        url = 'identity'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    def get_webhooks(self, page_size, cursor=None,  includes=None, fields=None):
        url = 'webhooks'
        params = {'page[count]': page_size}
        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            params.update({'page[cursor]': cursor})
        url += "?" + urlencode(params)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    def get_campaigns_by_id_members(self, resource_id, page_size, cursor=None,  includes=None, fields=None):
        url = 'campaigns/{}/members'.format(resource_id)
        params = {'page[count]': page_size}
        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            params.update({'page[cursor]': cursor})
        url += "?" + urlencode(params)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    def get_campaigns_by_id(self, resource_id, includes=None, fields=None):
        url = 'campaigns/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    def get_webhooks_by_id(self, resource_id, includes=None, fields=None):
        url = 'webhooks/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    def get_members_by_id(self, resource_id, includes=None, fields=None):
        url = 'members/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )

    @staticmethod
    def extract_cursor(jsonapi_document, cursor_path='links.next'):
        def head_and_tail(path):
            if path is None:
                return None, None
            head_tail = path.split('.', 1)
            return head_tail if len(head_tail) == 2 else (head_tail[0], None)

        if isinstance(jsonapi_document, JSONAPIParser):
            jsonapi_document = jsonapi_document.json_data

        head, tail = head_and_tail(cursor_path)
        current_dict = jsonapi_document
        while head and type(current_dict) == dict and head in current_dict:
            current_dict = current_dict[head]
            head, tail = head_and_tail(tail)

        # Path was valid until leaf, at which point nothing was found
        if current_dict is None or (head is not None and tail is None):
            return None

        elif type(current_dict) == dict and head not in current_dict:
            return None

        # Path stopped before leaf was reached
        elif current_dict and type(current_dict) != six.text_type:
            raise Exception(
                'Provided cursor path did not result in a link', current_dict
            )

        link = current_dict
        query_string = urlparse(link).query
        parsed_query_string = parse_qs(query_string)
        if 'page[cursor]' in parsed_query_string:
            return parsed_query_string['page[cursor]'][0]
        else:
            return None

    # Internal methods
    def __get_jsonapi_doc(self, suffix):
        response_json = self.__get_json(suffix)
        if response_json.get('errors'):
            return response_json
        return JSONAPIParser(response_json)

    def __get_json(self, suffix):
        response = requests.get(
            "https://www.patreon.com/api/oauth2/v2/{}".format(suffix),
            headers={
                'Authorization': "Bearer {}".format(self.access_token),
                'User-Agent': user_agent_string(),
            }
        )
        return response.json()

    @staticmethod
    def __as_utc(dt):
        if hasattr(dt, 'tzinfo'):
            if dt.tzinfo:
                return dt.astimezone(utc_timezone())
            else:
                return dt.replace(tzinfo=utc_timezone())
        return dt
