# patreon-python
Interact with the Patreon API via OAuth.

Get the egg from [PyPI](https://pypi.python.org/pypi/patreon)

Step 1. Get your client_id and client_secret
---
Visit the [OAuth Documentation Page](https://www.patreon.com/oauth2/documentation)
while logged in as a Patreon creator to register your client.

This will provide you with a `client_id` and a `client_secret`.

Step 2. Use this library
---
e.g., in a Flask route
```python
import patreon
from flask import request
...

client_id = None      # Replace with your data
client_secret = None  # Replace with your data
creator_id = None     # Replace with your data

@app.route('/oauth/redirect')
def oauth_redirect():
    oauth_client = patreon.OAuth(client_id, client_secret)
    tokens = oauth_client.get_tokens(request.args.get('code'), redirect_uri)
    access_token = tokens['access_token']

    api_client = patreon.API(access_token)
    user_response = api_client.fetch_user()
    user = user_response['data']
    included = user_response.get('included')
    if included:
      pledge = next((obj for obj in included
        if obj['type'] == 'pledge' and obj['relationships']['creator']['data']['id'] == creator_id), None)
      campaign = next((obj for obj in included
        if obj['type'] == 'campaign' and obj['relationships']['creator']['data']['id'] == creator_id), None)
    else:
      pledge = nil
      campaign = nil

    # pass user, pledge, and campaign to your view to render as needed
```
