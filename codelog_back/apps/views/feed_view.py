from flask import Blueprint
from flask import abort
from flask import request
from marshmallow.exceptions import ValidationError

from apps.schemas import CreateFeedRequestSchema
from apps.usecases import GetFeedListUsecase, CreateFeedUsecase
from typing import NoReturn, Union
from apps.entities import FeedEntity
from apps.presenters import GetFeedListPresenter, CreateFeedPresenter

feed_bp = Blueprint('feeds', __name__, url_prefix='/api/feeds')


@feed_bp.route('/', methods=['GET'])
def get_feed_list():
    feeds = GetFeedListUsecase().execute()
    return GetFeedListPresenter.transform(response=feeds)


@feed_bp.route('/', methods=['POST'])
def create_feed() -> Union[NoReturn, FeedEntity]:
    try:
        validator = CreateFeedRequestSchema().load(data=request.form)
    except ValidationError:
        abort(400, 'validation error')

    feed = CreateFeedUsecase().execute(
        **validator,
        auth_header=request.headers.get('Authorization'),
    )

    return CreateFeedPresenter.transform(response=feed)
