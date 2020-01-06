from dataclasses import dataclass
from datetime import datetime


@dataclass
class FeedEntity:
    id: int = None
    user_id: int = None
    image: str = None
    title: str = None
    description: str = None
    url: str = None
    created_at: datetime = None
    updated_at: datetime = None
