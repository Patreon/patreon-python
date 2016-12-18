import os


def _db_file_location():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "../sqlite.db")

database = {
    'location': 'sqlite:///' + _db_file_location()
}

port = 5000
