from flask import Blueprint


user_bp = Blueprint('users', __name__, url_prefix='/api/users')


@user_bp.route('/')
def hello():
    return 'Hello'
