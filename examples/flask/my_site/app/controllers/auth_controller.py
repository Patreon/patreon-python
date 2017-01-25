#!flask/bin/python
from flask import Blueprint, request, abort, redirect
import patreon

from my_site import config
from my_site.app.views.html_renderer import render_page
from my_site.app.views.LogIn.log_in import LogIn
from my_site.app.views.LandingPage.landing_page import LandingPage
from my_site.models.managers import patreon_user_mgr
from my_site.models.tables.user import User

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/', methods=['GET'])
def landing_page():
    # https://www.patreon.com/platform/documentation/oauth -- Step 1
    # The landing page links to patreon.com/oauth2/authorize so the user can authorize this app to access their Patreon data.
    return render_page(
        inner=LogIn
    )


@auth_blueprint.route('/oauth/redirect', methods=['GET'])
def oauth_redirect():
    # https://www.patreon.com/platform/documentation/oauth -- Step 2
    # After authorizing this app to access their Patreon data, the user is redirected back here.

    # https://www.patreon.com/platform/documentation/oauth -- Step 3
    # Use the code provided as a query parameter to get the user's access token and refresh token
    oauth_client = patreon.OAuth(config.patreon_client_id, config.patreon_client_secret)
    tokens = oauth_client.get_tokens(request.args.get('code'), 'http://localhost:5000/oauth/redirect')

    # https://www.patreon.com/platform/documentation/oauth -- Step 4
    # Save off the user's tokens and fetch their Patreon data.
    user = patreon_user_mgr.update_user_for_tokens(
        patreon_refresh_token=tokens['refresh_token'],
        patreon_access_token=tokens['access_token']
    )

    # https://www.patreon.com/platform/documentation/oauth -- Step 5
    # If the user signed in successfully, take them to their profile page.
    if user:
        return redirect('/users/{user_id}'.format(user_id=user.user_id))
    else:
        abort(403)


@auth_blueprint.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    user = User.get(user_id)
    if not user:
        abort(404)
    return render_page(
        inner=LandingPage,
        user=user
    )
