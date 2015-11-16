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

  def __get_json(self, suffix):
    response = requests.get("https://api.patreon.com/oauth2/api/{}".format(suffix),
      headers={'Authorization': "Bearer {}".format(self.access_token)})
    return response.json()
