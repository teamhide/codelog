from sqlalchemy import (Column, BigInteger, Unicode)

from core.databases import Base
from core.databases.mixin import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(Unicode(255))
    login_type = Column(Unicode(20), nullable=False)
    access_token = Column(Unicode(255), nullable=False)
    refresh_token = Column(Unicode(255), nullable=False)
