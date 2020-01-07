import re
from dataclasses import dataclass
from typing import Union

import requests
from flask import abort

from apps.enums import LoginType
from apps.repositories import UserMySQLRepo
from core.settings import OAuthConfig
from core.utils import TokenHelper


@dataclass(frozen=True)
class Token:
    token: str = None
    refresh_token: str = None


class UserUsecase:
    def __init__(self):
        self.user_repo = UserMySQLRepo()

    def _create_refresh_token(self) -> str:
        return TokenHelper.encode(
            payload={'sub': 'refresh'},
            expire_period=86400,
        ).decode('utf8')


class GithubLoginUsecase(UserUsecase):
    def execute(self, code: str) -> Union[Token, abort]:
        response = requests.post(
            url='https://github.com/login/oauth/access_token',
            data={
                'code': code,
                'client_id': OAuthConfig.github_client_id,
                'client_secret': OAuthConfig.github_client_secret,
                'redirect_uri': OAuthConfig.github_redirect_uri,
            }
        )
        pattern = 'access_token=(\w+)'
        github_access_token = re.findall(pattern, response.text)[0]

        response = requests.get(
            url='https://api.github.com/user',
            headers={
                'Authorization': f'token {github_access_token}'
            }
        ).json()
        nickname = response.get('login')
        avatar_url = response.get('avatar_url')
        email = response.get('email')

        if not email:
            abort(400, 'email required')

        user = self.user_repo.get_user(email=email, login_type='github')
        refresh_token = self._create_refresh_token()

        if user:
            self.user_repo.update_token(
                access_token=github_access_token,
                email=email,
                login_type='github',
            )
        else:
            user = self.user_repo.save_user(
                email=email,
                login_type='github',
                access_token=github_access_token,
                refresh_token=refresh_token,
                avatar_url=avatar_url,
            )

        token = TokenHelper.encode(payload={'user_id': user.id})

        return Token(
            token=token.decode('utf8'),
            refresh_token=refresh_token,
        )


class GoogleLoginUsecase(UserUsecase):
    def execute(self, code: str) -> Union[Token, abort]:
        response = requests.post(
            url='https://www.googleapis.com/oauth2/v4/token',
            data={
                'code': code,
                'client_id': OAuthConfig.google_client_id,
                'client_secret': OAuthConfig.google_client_secret,
                'redirect_uri': OAuthConfig.google_redirect_uri,
                'grant_type': 'authorization_code',
            },
        )
        google_access_token = response.json().get('access_token')
        id_token = response.json().get('id_token')

        if not google_access_token or not id_token:
            abort(400, 'get token error')

        response = requests.get(
            url=f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}'
        )
        email = response.json().get('email')

        if not email:
            abort(400, 'email required')

        user = self.user_repo.get_user(
            email=email,
            login_type=LoginType.GOOGLE,
        )

        refresh_token = TokenHelper.encode(
            payload={'sub': 'refresh'},
            expire_period=86400,
        )

        if user:
            # TODO: Update user info
            pass
        else:
            # TODO: Create user
            pass

        token = TokenHelper.encode(payload={'user_id': user.id})

        return Token(token=token, refresh_token=refresh_token)


class KakaoLoginUsecase(UserUsecase):
    def execute(self, code: str) -> Union[Token, abort]:
        pass
