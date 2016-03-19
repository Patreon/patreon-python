import urllib
from datetime import timezone
from urllib.parse import parse_qs, urlparse

import requests


class API(object):

    def __init__(self, access_token):
        super(API, self).__init__()
        self.access_token = access_token

    def fetch_user(self):
        return self.__get_json('current_user')

    def fetch_campaign_and_patrons(self):
        return self.__get_json('current_user/campaigns?include=rewards,creator,goals,pledges')

    def fetch_campaign(self):
        return self.__get_json('current_user/campaigns?include=rewards,creator,goals')

    def fetch_page_of_pledges(self, campaign_id, page_size, cursor=None, return_cursor=False):
        url = 'campaigns/{0}/pledges?page%5Bcount%5D={1}'.format(campaign_id, str(page_size))

        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            url += '&page%5Bcursor%5D={0}'.format(urllib.parse.quote(cursor))

        if return_cursor:
            data = self.__get_json(url)

            # Extract the 'cursor'
            if 'next' in data['links']:
                query_string = urlparse(data['links']['next']).query
                parsed_query_string = parse_qs(query_string)
                cursor = parsed_query_string['page[cursor]'][0]

            return data, cursor
        return self.__get_json(url)

    def __get_json(self, suffix):
        response = requests.get("https://api.patreon.com/oauth2/api/{}".format(suffix), headers={
            'Authorization': "Bearer {}".format(self.access_token)
        })
        return response.json()

    @staticmethod
    def __as_utc(dt):
        if hasattr(dt, 'tzinfo'):
            if dt.tzinfo:
                return dt.astimezone(timezone.utc)
            else:
                return dt.replace(tzinfo=timezone.utc)
        return dt
