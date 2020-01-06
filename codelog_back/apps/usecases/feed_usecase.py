import re
from dataclasses import dataclass
from typing import List

import requests
from flask import abort

from apps.entities import FeedEntity
from apps.repositories import FeedMySQLRepo, UserMySQLRepo
from core.settings import get_config
from core.utils import TokenHelper


@dataclass
class OGTag:
    title: str = None
    image: str = None
    description: str = None


class FeedUsecase:
    def __init__(self):
        self.feed_repo = FeedMySQLRepo()
        self.user_repo = UserMySQLRepo()

    def parse(self, url: str) -> OGTag:
        try:
            r = requests.get(url=url, headers=get_config().request_headers)
        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.MissingSchema,
        ):
            abort(400, 'incorrect url')

        ogtag = OGTag()

        title_pattern = '"og:title" content="(.+?)"'
        ogtag.title = re.findall(title_pattern, r.text)

        image_pattern = '"og:image" content="(.+?)"'
        ogtag.image = re.findall(image_pattern, r.text)

        description_pattern = '"og:description" content="(.+?)"'
        ogtag.description = re.findall(description_pattern, r.text)

        return ogtag


class GetFeedListUsecase(FeedUsecase):
    def execute(self) -> List[FeedEntity]:
        feeds = self.feed_repo.get_feed_list()
        return feeds


class CreateFeedUsecase(FeedUsecase):
    def execute(self, url: str, tags: str, auth_header: str) -> FeedEntity:
        # Check
        if not auth_header:
            abort(400, 'token header error')

        # Extract payload from token
        payload = TokenHelper.decode(token=auth_header.split()[1])
        user = self.user_repo.get_user(user_id=int(payload['user_id']))

        if not user:
            abort(400, 'user does not exist')

        # Get og tag info
        og_info = self.parse(url=url)

        # Create feed
        feed = self.feed_repo.create_feed(
            user_id=user.id,
            url=url,
            tags=tags.split(','),
            image=og_info.image,
            title=og_info.title,
            description=og_info.description,
        )

        return feed
