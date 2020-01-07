from flask import Blueprint, request
from apps.usecases import (
    GithubLoginUsecase,
    GoogleLoginUsecase,
    KakaoLoginUsecase,
)
from apps.presenters import OAuthLoginResponsePresenter


oauth_bp = Blueprint('oauth', __name__, url_prefix='/oauth')


@oauth_bp.route('/github/login', methods=['GET'])
def github_login():
    token = GithubLoginUsecase().execute(code=request.args.get('code'))
    return OAuthLoginResponsePresenter.transform(response=token)


@oauth_bp.route('/google/login', methods=['GET'])
def google_login():
    token = GoogleLoginUsecase().execute(code=request.args.get('code'))
    return {'status': True}


@oauth_bp.route('/kakao/login', methods=['GET'])
def kakao_login():
    token = KakaoLoginUsecase().execute(code=request.args.get('code'))
    return 'Hello'
