import abc
from flask import jsonify


class Presenter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def transform(self, response) -> jsonify:
        pass
