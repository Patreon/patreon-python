from my_site.app.views import base_view


class LandingPage(base_view.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs['user']

    def data(self):
        return {
            'full_name': self.user.full_name,
            'email': self.user.email,
            'pledge_amount_cents': self.user.patreon_pledge_amount_cents,
        }

    def template(self):
        return 'LandingPage/landing_page.html'
