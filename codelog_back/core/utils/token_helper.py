from datetime import datetime, timedelta

import jwt
from flask import abort

from core.settings import get_config


class TokenHelper:
    @classmethod
    def decode(cls, token: str) -> dict:
        try:
            return jwt.decode(
                token,
                get_config().jwt_secret_key,
                algorithms=[get_config().jwt_algorithm],
            )
        except jwt.exceptions.DecodeError:
            abort(401, 'token decode error')
        except (jwt.exceptions.InvalidTokenError, jwt.exceptions.InvalidSignatureError):
            abort(401, 'invalid token')
        except jwt.exceptions.ExpiredSignatureError:
            abort(401, 'token expired')

    @classmethod
    def encode(cls, payload: dict, expire_period: int = 3600):
        return jwt.encode(
            payload={
                **payload,
                'exp': datetime.utcnow() + timedelta(seconds=expire_period),
            },
            key=get_config().jwt_secret_key,
            algorithm=get_config().jwt_algorithm,
        )
