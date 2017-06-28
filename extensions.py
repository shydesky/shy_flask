# -*- coding: utf-8 -*-
import types
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

api = Api()
db = SQLAlchemy()
migrate = Migrate()


def api_route(self, *args, **kwargs):
    u"""给flask api加上route功能，避免直接调用api.add_resource函数了.

    参考: http://flask.pocoo.org/snippets/129/
    """
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)
