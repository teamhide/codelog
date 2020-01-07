import abc
from typing import Optional
from typing import Union

from flask import abort

from apps.entities import UserEntity
from apps.models import User
from core.databases import session


class UserRepo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_user(
        self,
        user_id: int = None,
        email: str = None,
        login_type: str = None,
    ) -> Optional[UserEntity]:
        pass

    @abc.abstractmethod
    def save_user(
        self,
        email: str,
        nickname: str,
        login_type: str,
        access_token: str,
        refresh_token: str,
        avatar_url: str,
    ) -> Union[UserEntity, abort]:
        pass

    @abc.abstractmethod
    def update_token(
        self,
        email: str,
        login_type: str,
        access_token: str = None,
        refresh_token: str = None,
    ) -> Union[UserEntity, abort]:
        pass


class UserMySQLRepo(UserRepo):
    def get_user(
        self,
        user_id: int = None,
        email: str = None,
        login_type: str = None,
    ) -> Optional[UserEntity]:
        query = session.query(User)

        if user_id:
            query = query.filter(User.id == user_id)

        if email and login_type:
            query = query.filter(
                User.email == email,
                User.login_type == login_type,
            )

        user = query.first()

        if not user:
            return None

        return user.to_entity()

    def save_user(
        self,
        email: str,
        nickname: str,
        login_type: str,
        access_token: str,
        refresh_token: str,
        avatar_url: str,
    ) -> Union[UserEntity, abort]:
        user = User(
            email=email,
            login_type=login_type,
            nickname=nickname,
            avatar_url=avatar_url,
        )

        if not access_token and refresh_token:
            abort(500, 'access_token and refresh_token is empty')

        if access_token:
            user.access_token = access_token

        if refresh_token:
            user.refresh_token = refresh_token

        session.add(user)
        session.commit()

        return user.to_entity()

    def update_token(
        self,
        email: str,
        login_type: str,
        access_token: str = None,
        refresh_token: str = None,
    ) -> Union[UserEntity, abort]:
        user = session.query(User).filter(
            User.email == email,
            User.login_type == login_type,
        ).first()

        if not access_token and not refresh_token:
            abort(500, 'access_token and refresh_token is empty')

        if access_token:
            user.access_token = access_token

        if refresh_token:
            user.refresh_token = refresh_token

        session.add(user)
        session.commit()

        return user.to_entity()
