import os
from flask import Flask
from flask.helpers import get_debug_flag
from extensions import api, db, migrate
from shy_flask import (module1)
from settings import ProdConfig, DevConfig


def register_extensions(app):
    api.init_app(app)
    db.init_app(app)
    migrate.init(app)


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object('config')
    register_extensions(app)
    return app


def which_config():
    u"""在环境变量中导出USE_CONFIG决定使用哪个配置."""
    config_dict = {
        'prod': ProdConfig,
        'dev': DevConfig,
    }
    environ = os.environ.get('USE_CONFIG', 'dev')
    config = config_dict.get(environ)
    is_debug = get_debug_flag()
    config = (config or DevConfig) if is_debug else config
    return config

config = which_config()
app = create_app(config_object=config)





if __name__ == '__main__':
    app.run(host='0.0.0.0')
