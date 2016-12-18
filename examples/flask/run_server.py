#!venv/bin/python
from my_site.app import create_app
from my_site import config


my_app = create_app()
my_app.run(debug=True, host='0.0.0.0', port=config.port)
