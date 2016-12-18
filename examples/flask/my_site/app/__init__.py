from flask import Flask, jsonify, make_response

import my_site
from my_site.app.views import configure_jinja
from my_site.models.flask.my_request import MyRequest
from my_site.models.flask.my_session import MySessionInterface
from my_site.models.tables import (
    db,
    db_wrapper,
)


def json_error_description(error_):
    if hasattr(error_, 'description') and hasattr(error_, 'code'):
        return make_response(jsonify({'error': error_.description}), error_.code)
    else:
        return make_response(jsonify({'error': str(error_)}), 500)


def create_app() -> Flask:
    my_app = Flask(__name__)

    # Configure sessions
    my_app.session_interface = MySessionInterface()
    my_app.request_class = MyRequest

    # Configure Jinja
    configure_jinja.configure(my_app)

    # Configure db
    my_app.config['SQLALCHEMY_DATABASE_URI'] = my_site.config.database['location']
    db.init_app(my_app)
    with my_app.app_context():
        db_wrapper.build_if_needed(db)

    # Configure routing & controllers
    # import and register all controllers here
    from .controllers import (
        auth_controller
    )
    my_app.register_blueprint(auth_controller.auth_blueprint)

    # Configure error handling
    for error in list(range(400, 420)) + list(range(500, 506)):
        my_app.error_handler_spec[None][error] = json_error_description

    return my_app
