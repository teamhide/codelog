from flask import Flask

from apps.views import feed_bp, user_bp
from core.databases import session
from flask_cors import CORS


def init_listeners(app: Flask):
    @app.after_request
    def after_request(response):
        session.remove()
        return response


def init_middlewares(app: Flask):
    pass


def init_blueprint(app: Flask):
    app.register_blueprint(feed_bp)
    app.register_blueprint(user_bp)


def init_extensions(app: Flask):
    CORS(app)


def create_app():
    app = Flask(__name__)
    init_blueprint(app=app)
    init_listeners(app=app)
    init_extensions(app=app)
    return app
