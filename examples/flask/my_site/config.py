import os


def _db_file_location():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "../sqlite.db")

database = {
    'location': 'sqlite:///' + _db_file_location()
}

port = 5000

patreon_client_id = os.environ.get('PATREON_CLIENT_ID')
patreon_client_secret = os.environ.get('PATREON_CLIENT_SECRET')
patreon_redirect_uri = 'http://localhost:5000/oauth/redirect'
oauth_csrf = os.environ.get('OAUTH_CSRF', 'givecreatorschoice')
