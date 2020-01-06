from flask import Flask

from core.databases import session


def init_listeners(app: Flask):
    @app.after_request
    def after_request(response):
        session.remove()
        return response


def init_middlewares(app: Flask):
    pass


def init_blueprint(app: Flask):
    pass
    # app.register_blueprint(home_bp)
    # app.register_blueprint(post_bp_v1, url_prefix='/api/v1/posts/')
    # app.register_blueprint(user_bp_v1, url_prefix='/api/v1/users/')


def init_extensions(app: Flask):
    pass


def create_app():
    app = Flask(__name__)
    init_blueprint(app=app)
    init_listeners(app=app)
    return app
