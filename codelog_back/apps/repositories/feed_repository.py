import abc
from typing import List, Union

from sqlalchemy import or_

from apps.entities import FeedEntity, TagEntity
from apps.models import Feed, Tag
from core.databases import session


class FeedRepo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_feed_list(self) -> List[FeedEntity]:
        pass

    @abc.abstractmethod
    def create_feed(
        self,
        user_id: int,
        url: str,
        tags: List,
        image: str,
        title: str,
        description: str,
    ) -> FeedEntity:
        pass

    @abc.abstractmethod
    def create_tag(self, name: Union[str, List], many: bool = False) -> None:
        pass

    @abc.abstractmethod
    def get_tag_list(self) -> List[TagEntity]:
        pass

    @abc.abstractmethod
    def search_feed(
        self,
        keyword: str,
        prev: int = None,
    ) -> List[FeedEntity]:
        pass


class FeedMySQLRepo(FeedRepo):
    def get_feed_list(self) -> List[FeedEntity]:
        feeds = session.query(Feed).order_by(Feed.id.desc()).limit(20).all()
        return [
            feed.to_entity()
            for feed in feeds
        ]

    def create_feed(
        self,
        user_id: int,
        url: str,
        tags: List,
        image: str,
        title: str,
        description: str,
    ) -> FeedEntity:
        feed = Feed(
            user_id=user_id,
            url=url,
            image=image,
            title=title,
            description=description,
        )

        for tag in tags:
            exist = session.query(Tag).filter(Tag.name == tag).first()
            if exist:
                feed.tags.append(exist)
            else:
                feed.tags.append(Tag(name=tag))

        session.add(feed)
        session.commit()

        return feed.to_entity()

    def create_tag(self, name: Union[str, List], many: bool = False) -> None:
        if many is True:
            tags = [
                row[0]
                for row in session.query(Tag)
                .filter(Tag.name.in_(name)).with_entities(Tag.name).all()
            ]
            for tag in list(set(name) - set(tags)):
                session.add(Tag(name=tag))
        else:
            pass

        session.commit()

    def get_tag_list(self) -> List[TagEntity]:
        tags = session.query(Tag).all()

        return [
            tag.to_entity()
            for tag in tags
        ]

    def search_feed(
        self,
        keyword: str,
        prev: int = None,
    ) -> List[FeedEntity]:
        query = session.query(Feed)

        query = query.filter(
            or_(
                Feed.title.like(f'%{keyword}%'),
                Feed.description.like(f'%{keyword}%'),
            ),
        )

        feeds = query.order_by(Feed.id.desc()).limit(20)

        return [
            feed.to_entity()
            for feed in feeds
        ]
