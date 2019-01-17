# api_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import datetime
import functools
import mock
import six

from patreon import api
from patreon.jsonapi import url_util
from patreon.jsonapi.parser import JSONAPIParser
from patreon.utils import user_agent_string
from patreon.version_compatibility.utc_timezone import utc_timezone
from six.moves.urllib.parse import urlencode

MOCK_ID = 12
API_ROOT_ENDPOINT =  'https://www.patreon.com/api/oauth2/v2/'
MOCK_ACCESS_TOKEN =  'mock token'
MOCK_CURSOR_VALUE =  'Mock Cursor Value'
PAGE_COUNT = 25


DEFAULT_API_HEADERS = {
    'Authorization': 'Bearer ' + MOCK_ACCESS_TOKEN,
    'User-Agent': user_agent_string(),
}

client = api.API(access_token=MOCK_ACCESS_TOKEN)


def api_url(*segments, **query):
    path = '/'.join(map(str, segments))

    fields = query.get('fields', None)
    includes = query.get('includes', None)

    if fields:
        del query['fields']

    if includes:
        del query['includes']

    if query:
        path += '?' + urlencode(query)

    return url_util.build_url(
        API_ROOT_ENDPOINT + path,
        fields=fields,
        includes=includes,
    )


def assert_valid_api_call(method, api_url, query=None, **kwargs):
    kwargs.setdefault('headers', DEFAULT_API_HEADERS)
    method.assert_called_once_with(api_url, **kwargs)


class MockResponse(object):
    def __init__(self, data=None, status_code=200):
        self.data = data or {}

        self.status_code = status_code

    def json(self):
        return self.data


def api_test(method='GET', **response_kwargs):
    """ Decorator to ensure API calls are made and return expected data. """

    method = method.lower()

    def api_test_factory(fn):
        @functools.wraps(fn)
        @mock.patch('requests.{}'.format(method))
        def execute_test(method_func, *args, **kwargs):
            method_func.return_value = MockResponse(**response_kwargs)

            expected_url, response = fn(*args, **kwargs)

            method_func.assert_called_once()
            assert_valid_api_call(method_func, expected_url)
            assert isinstance(response, JSONAPIParser)
            assert response.json_data is method_func.return_value.data

        return execute_test

    return api_test_factory


def test_extract_cursor_returns_cursor_when_provided():
    assert MOCK_CURSOR_VALUE == api.API.extract_cursor(
        {
             six.text_type('links'):
                {
                     six.text_type('next'):
                         six.text_type('https://patreon.com/members?page[cursor]=') +
                        MOCK_CURSOR_VALUE,
                },
        }
    )


def test_extract_cursor_returns_None_when_no_cursor_provided():
    assert None is api.API.extract_cursor(
        {
             six.text_type('links'): {
                 six.text_type('next'):  six.text_type('https://patreon.com/members?page[offset]=25'),
            },
        }
    )


def test_extract_cursor_returns_None_when_link_is_not_a_string():
    assert None is api.API.extract_cursor({
         'links': {
             'next': None,
        },
    })


def test_extract_cursor_returns_None_when_link_is_malformed():
    caught_exception = False

    try:
        api.API.extract_cursor({
             'links': {
                 'next': 12,
            },
        })

    except Exception as e:
        caught_exception = True
        assert e.args[0] == 'Provided cursor path did not result in a link'

    assert caught_exception


@api_test()
def test_get_campaigns():
    url = 'campaigns'
    query_params = {'page[count]': PAGE_COUNT}
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns(
        PAGE_COUNT,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_with_includes():
    url = 'campaigns'
    query_params = {'page[count]': PAGE_COUNT}
    expected_url = api_url(url, includes=['mock'], **query_params)
    response = client.get_campaigns(
        PAGE_COUNT,
        includes=['mock']
    )

    return expected_url, response

@api_test()
def test_get_campaigns_with_arbitrary_cursor():
    url = 'campaigns'
    query_params = {'page[count]': PAGE_COUNT, 'page[cursor]': MOCK_CURSOR_VALUE}
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns(
                PAGE_COUNT,
        cursor=MOCK_CURSOR_VALUE,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_with_custom_options_without_tzinfo():
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.replace(tzinfo=utc_timezone()).isoformat()
    url = 'campaigns'
    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns(
                PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    return expected_url, response


def test_get_campaigns_with_custom_options_without_tzinfo():
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.isoformat()
    url = 'campaigns'
    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns(
                PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    return expected_url, response


@api_test()
def test_get_identity():
    url = 'identity'
    expected_url = api_url(url)
    response = client.get_identity()

    return expected_url, response


@api_test()
def test_get_identity_with_includes():
    url = 'identity'
    expected_url = api_url(url, includes=['mock'])
    response = client.get_identity(includes=['mock'])

    return expected_url, response



@api_test()
def test_get_webhooks():
    url = 'webhooks'
    query_params = {'page[count]': PAGE_COUNT}
    expected_url = api_url(url, **query_params)
    response = client.get_webhooks(
        PAGE_COUNT,
    )

    return expected_url, response


@api_test()
def test_get_webhooks_with_includes():
    url = 'webhooks'
    query_params = {'page[count]': PAGE_COUNT}
    expected_url = api_url(url, includes=['mock'], **query_params)
    response = client.get_webhooks(
        PAGE_COUNT,
        includes=['mock']
    )

    return expected_url, response

@api_test()
def test_get_webhooks_with_arbitrary_cursor():
    url = 'webhooks'
    query_params = {'page[count]': PAGE_COUNT, 'page[cursor]': MOCK_CURSOR_VALUE}
    expected_url = api_url(url, **query_params)
    response = client.get_webhooks(
                PAGE_COUNT,
        cursor=MOCK_CURSOR_VALUE,
    )

    return expected_url, response


@api_test()
def test_get_webhooks_with_custom_options_without_tzinfo():
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.replace(tzinfo=utc_timezone()).isoformat()
    url = 'webhooks'
    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }
    expected_url = api_url(url, **query_params)
    response = client.get_webhooks(
                PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    return expected_url, response


def test_get_webhooks_with_custom_options_without_tzinfo():
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.isoformat()
    url = 'webhooks'
    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }
    expected_url = api_url(url, **query_params)
    response = client.get_webhooks(
                PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_by_id_members():
    url = 'campaigns/{}/members'.format(MOCK_ID)
    query_params = {'page[count]': PAGE_COUNT}
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns_by_id_members(
        MOCK_ID,
        PAGE_COUNT,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_by_id_members_with_includes():
    url = 'campaigns/{}/members'.format(MOCK_ID)
    query_params = {'page[count]': PAGE_COUNT}
    expected_url = api_url(url, includes=['mock'], **query_params)
    response = client.get_campaigns_by_id_members(
        MOCK_ID,
        PAGE_COUNT,
        includes=['mock']
    )

    return expected_url, response

@api_test()
def test_get_campaigns_by_id_members_with_arbitrary_cursor():
    url = 'campaigns/{}/members'.format(MOCK_ID)
    query_params = {'page[count]': PAGE_COUNT, 'page[cursor]': MOCK_CURSOR_VALUE}
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns_by_id_members(
        MOCK_ID,         PAGE_COUNT,
        cursor=MOCK_CURSOR_VALUE,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_by_id_members_with_custom_options_without_tzinfo():
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.replace(tzinfo=utc_timezone()).isoformat()
    url = 'campaigns/{}/members'.format(MOCK_ID)
    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns_by_id_members(
        MOCK_ID,         PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    return expected_url, response


def test_get_campaigns_by_id_members_with_custom_options_without_tzinfo():
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.isoformat()
    url = 'campaigns/{}/members'.format(MOCK_ID)
    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }
    expected_url = api_url(url, **query_params)
    response = client.get_campaigns_by_id_members(
        MOCK_ID,         PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_by_id():
    url = 'campaigns/{}'.format(MOCK_ID)
    expected_url = api_url(url)
    response = client.get_campaigns_by_id(
        MOCK_ID,
    )

    return expected_url, response


@api_test()
def test_get_campaigns_by_id_with_includes():
    url = 'campaigns/{}'.format(MOCK_ID)
    expected_url = api_url(url, includes=['mock'])
    response = client.get_campaigns_by_id(
        MOCK_ID,
        includes=['mock']
    )

    return expected_url, response



@api_test()
def test_get_webhooks_by_id():
    url = 'webhooks/{}'.format(MOCK_ID)
    expected_url = api_url(url)
    response = client.get_webhooks_by_id(
        MOCK_ID,
    )

    return expected_url, response


@api_test()
def test_get_webhooks_by_id_with_includes():
    url = 'webhooks/{}'.format(MOCK_ID)
    expected_url = api_url(url, includes=['mock'])
    response = client.get_webhooks_by_id(
        MOCK_ID,
        includes=['mock']
    )

    return expected_url, response



@api_test()
def test_get_members_by_id():
    url = 'members/{}'.format(MOCK_ID)
    expected_url = api_url(url)
    response = client.get_members_by_id(
        MOCK_ID,
    )

    return expected_url, response


@api_test()
def test_get_members_by_id_with_includes():
    url = 'members/{}'.format(MOCK_ID)
    expected_url = api_url(url, includes=['mock'])
    response = client.get_members_by_id(
        MOCK_ID,
        includes=['mock']
    )

    return expected_url, response

