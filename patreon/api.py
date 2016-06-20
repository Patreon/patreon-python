import requests

from patreon.jsonapi.url_util import build_url
from patreon.schemas import campaign
from patreon.version_compatibility.utc_timezone import utc_timezone
from patreon.version_compatibility.urlencode import urlencode


class API(object):
  def __init__(self, access_token):
    super(API, self).__init__()
    self.access_token = access_token

  def fetch_user(self, includes=None, fields=None):
    return self.__get_json(build_url('current_user', includes=includes, fields=fields))

  def fetch_campaign_and_patrons(self, includes=None, fields=None):
    if not includes:
      includes = campaign.default_relationships + [campaign.Relationships.pledges]
    return self.fetch_campaign(includes=includes, fields=fields)

  def fetch_campaign(self, includes=None, fields=None):
    return self.__get_json(build_url('current_user/campaigns', includes=includes, fields=fields))

  def fetch_page_of_pledges(self, campaign_id, page_size, cursor=None, includes=None, fields=None):
    url = 'campaigns/{0}/pledges'.format(campaign_id)
    params = {'page[count]': page_size}
    if cursor:
      try:
        cursor = self.__as_utc(cursor).isoformat()
      except AttributeError:
        pass
      params.update({'page[cursor]': cursor})
    url += "?" + urlencode(params)
    return self.__get_json(build_url(url, includes=includes, fields=fields))

  def __get_json(self, suffix):
    response = requests.get(
      "https://api.patreon.com/oauth2/api/{}".format(suffix),
      headers={'Authorization': "Bearer {}".format(self.access_token)}
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
