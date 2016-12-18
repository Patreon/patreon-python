from flask.sessions import SessionMixin, SecureCookieSessionInterface


class MySession(dict, SessionMixin):
    def __init__(self, user_id=None, **kwargs):
        super().__init__(**kwargs)
        self['user_id'] = user_id

    @property
    def user_id(self):
        return self['user_id']


class MySessionInterface(SecureCookieSessionInterface):
    session_class = MySession
    salt = 'my-cookie-session'
