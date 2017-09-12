import datetime
import functools
import mock

from patreon import api
from patreon.jsonapi import url_util
from patreon.version_compatibility import urllib_parse
from patreon.version_compatibility.utc_timezone import utc_timezone

MOCK_CAMPAIGN_ID = 12
API_ROOT_ENDPOINT = 'https://api.patreon.com/oauth2/api/'
MOCK_ACCESS_TOKEN = 'mock token'

DEFAULT_API_HEADERS = {'Authorization': 'Bearer ' + MOCK_ACCESS_TOKEN}

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
        path += '?' + urllib_parse.urlencode(query)

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
            assert response is method_func.return_value.data

        return execute_test

    return api_test_factory


@api_test()
def test_can_fetch_campaign():
    expected_url = api_url('current_user', 'campaigns')
    response = client.fetch_campaign()
    return expected_url, response


@api_test()
def test_can_fetch_api_and_patrons():
    response = client.fetch_campaign_and_patrons()

    expected_url = api_url(
        'current_user',
        'campaigns',
        includes=['rewards', 'creator', 'goals', 'pledges'],
    )

    return expected_url, response


@api_test()
def test_can_fetch_api_and_patrons_with_custom_includes():
    expected_url = api_url(
        'current_user',
        'campaigns',
        includes=['creator'],
    )

    response = client.fetch_campaign_and_patrons(
        includes=['creator'],
    )

    return expected_url, response


@api_test()
def test_can_fetch_page_of_pledges():
    PAGE_COUNT = 25

    response = client.fetch_page_of_pledges(MOCK_CAMPAIGN_ID, PAGE_COUNT)

    query_params = {'page[count]': PAGE_COUNT}

    expected_url = api_url(
        'campaigns', MOCK_CAMPAIGN_ID, 'pledges', **query_params
    )

    return expected_url, response


@api_test()
def test_can_fetch_page_of_pledges_with_arbitrary_cursor():
    PAGE_COUNT = 25
    MOCK_CURSOR = 'Mock Cursor'

    response = client.fetch_page_of_pledges(
        MOCK_CAMPAIGN_ID,
        PAGE_COUNT,
        cursor=MOCK_CURSOR,
    )

    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': MOCK_CURSOR,
    }

    expected_url = api_url(
        'campaigns', MOCK_CAMPAIGN_ID, 'pledges', **query_params
    )

    return expected_url, response


@api_test()
def test_can_fetch_page_of_pledges_with_custom_options():
    PAGE_COUNT = 25
    MOCK_CURSOR = datetime.datetime.now()
    MOCK_FIELDS = {'field': ['value']}
    MOCK_INCLUDES = ['mock includes']

    EXPECTED_CURSOR = MOCK_CURSOR.replace(tzinfo=utc_timezone()).isoformat()

    response = client.fetch_page_of_pledges(
        MOCK_CAMPAIGN_ID,
        PAGE_COUNT,
        cursor=MOCK_CURSOR,
        includes=MOCK_INCLUDES,
        fields=MOCK_FIELDS,
    )

    query_params = {
        'page[count]': PAGE_COUNT,
        'page[cursor]': EXPECTED_CURSOR,
        'includes': MOCK_INCLUDES,
        'fields': MOCK_FIELDS,
    }

    expected_url = api_url(
        'campaigns', MOCK_CAMPAIGN_ID, 'pledges', **query_params
    )

    return expected_url, response
