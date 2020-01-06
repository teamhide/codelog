import abc
from apps.entities import UserEntity
from core.databases import session
from apps.models import User


class UserRepo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_user(self, user_id: int) -> UserEntity:
        pass


class UserMySQLRepo(UserRepo):
    def get_user(self, user_id: int) -> UserEntity:
        user = session.query(User).filter(User.id == user_id).first()
        return user.to_entity()
