import re
from dataclasses import dataclass
from typing import List, Union

import requests

from apps.entities import FeedEntity
from apps.repositories import FeedMySQLRepo, UserMySQLRepo
from core.exceptions import abort
from core.settings import get_config


@dataclass
class OGTag:
    title: str = None
    image: str = None
    description: str = None


class FeedUsecase:
    def __init__(self):
        self.feed_repo = FeedMySQLRepo()
        self.user_repo = UserMySQLRepo()


class GetFeedListUsecase(FeedUsecase):
    def execute(self, prev: int = None) -> List[FeedEntity]:
        feeds = self.feed_repo.get_feed_list(prev=prev)
        return feeds


class CreateFeedUsecase(FeedUsecase):
    def execute(self, url: str, tags: str, payload: dict) -> FeedEntity:
        # Extract payload from token
        user = self.user_repo.get_user(user_id=payload['user_id'])

        if not user:
            abort(400, error='user does not exist')

        # Get og tag info
        og_info = self._parse(url=url)

        # Check tags is valid
        if self._process_tags(tags=tags) is False:
            abort(400, error='invalid tag')

        # Process tags
        tags = self._process_tags(tags=tags)

        # Create feed
        feed = self.feed_repo.create_feed(
            user_id=user.id,
            url=url,
            tags=tags[:3],
            image=og_info.image if og_info.image.startswith('http') else None,
            title=og_info.title[:50],
            description=og_info.description[:50],
        )

        return feed

    def _parse(self, url: str) -> OGTag:
        try:
            r = requests.get(url=url, headers=get_config().request_headers)
        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.MissingSchema,
        ):
            abort(400, error='incorrect url')

        ogtag = OGTag()

        title_pattern = '"og:title" content="(.+?)"'
        title = re.findall(title_pattern, r.text)[0]

        if title:
            ogtag.title = title
        else:
            ogtag.title = None

        image_pattern = '"og:image" content="(.+?)"'
        image = re.findall(image_pattern, r.text)[0]

        if image:
            ogtag.image = image
        else:
            ogtag.image = None

        description_pattern = '"og:description" content="(.+?)"'
        description = re.findall(description_pattern, r.text)[0]

        if description:
            ogtag.description = description
        else:
            ogtag.description = None

        return ogtag

    def _process_tags(self, tags: str) -> Union[List, bool]:
        if len(tags) > 100:
            return False

        tags = re.findall('#\w+\s*\w+', tags)

        for tag in tags:
            if len(tag) > 20:
                return False

        return tags


class GetTagListUsecase(FeedUsecase):
    def execute(self):
        return self.feed_repo.get_tag_list()


class SearchFeedUsecase(FeedUsecase):
    def execute(self, keyword: str, prev: int = None):
        return self.feed_repo.search_feed(keyword=keyword, prev=prev)
