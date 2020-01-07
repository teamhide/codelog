from flask import jsonify

from apps.schemas import OAuthLoginResponseSchema
from apps.usecases import Token
from core.presenters import Presenter


class OAuthLoginResponsePresenter(Presenter):
    @classmethod
    def transform(cls, response: Token) -> jsonify:
        return jsonify(OAuthLoginResponseSchema().dump(response))
