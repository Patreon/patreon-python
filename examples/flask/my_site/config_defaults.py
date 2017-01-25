import os


def _db_file_location():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "../sqlite.db")

database = {
    'location': 'sqlite:///' + _db_file_location()
}

port = 5000

patreon_client_id = None
patreon_client_secret = None
patreon_creator_refresh_token = None
patreon_creator_access_token = None
patreon_creator_id = None
patreon_redirect_uri = 'http://localhost:5000/oauth/redirect'
