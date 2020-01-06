from sqlalchemy import (Column, BigInteger, Unicode, ForeignKey)

from core.databases import Base
from core.databases.mixin import TimestampMixin


class Feed(Base, TimestampMixin):
    __tablename__ = 'feeds'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    image = Column(Unicode(255), nullable=True)
    title = Column(Unicode(255), nullable=True)
    description = Column(Unicode(255), nullable=True)
    url = Column(Unicode(255), nullable=False)
