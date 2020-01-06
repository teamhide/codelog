from dataclasses import dataclass
from datetime import datetime
from typing import List

from .user_entity import UserEntity


@dataclass
class FeedEntity:
    id: int = None
    user_id: int = None
    image: str = None
    title: str = None
    description: str = None
    url: str = None
    user: UserEntity = None
    tags: List = None
    created_at: datetime = None
    updated_at: datetime = None
