from my_site import config
from my_site.app.views import base_view


class LogIn(base_view.View):
    def data(self):
        log_in_url = (
            "https://www.patreon.com/oauth2/authorize"
            "?response_type=code"
            "&client_id={client_id}"
            "&redirect_uri={redirect_uri}"
        ).format(
            client_id=config.patreon_client_id,
            redirect_uri=config.patreon_redirect_uri
        )
        return {
            'log_in_url': log_in_url
        }

    def template(self):
        return 'LogIn/log_in.html'
