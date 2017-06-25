# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get(
        'CRM-BACKEND_SECRET', '5NyDfAe4Qa6W2sk2rBXwKSvgNTclj0Q8mOmP4YpbgM0='
    )
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SENTRY_DSN = 'http://3b8fd86a45b7421885134adb473146d4:a32176ef5dec4b62aab891cf9b03ea20@192.168.2.16:9000/4'    # 开发机
    SENTRY_DSN = 'http://d592a1c37a92417d871466dfc1abb204:ba7392f628ac4004ad194fe479617ab0@172.16.1.173:9000/4'
    WTF_CSRF_ENABLED = False

    # For mail service
    MAIL_SERVER = 'email-smtp.us-east-1.amazonaws.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'AKIAJAR3YV3AKPHIAS6A'
    MAIL_PASSWORD = 'Ajf4f3lk2mSmywvygZ+Z3Jt7rnwgPPkqDqImbdUr1oor'
    MAIL_SUPPRESS_SEND = False
    MAIL_DEBUG = False
    BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

    REDSHIFT_URL = None

    REDIS_URL = "redis://@localhost:6379/0"    # TODO


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    DB_USER = 'root'
    DB_PASSWORD = 'q1w2e3r4'
    DB_NAME = 'crm_prod'
    DB_PATH = 'crm-prod.cjfrqij7amkp.us-west-1.rds.amazonaws.com'
    DB_PORT = 3306
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (
        DB_USER, DB_PASSWORD, DB_PATH, DB_PORT, DB_NAME
    )
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar

    SQLALCHEMY_BINDS = {
        'redshift': 'postgres://appfloodcode:Papaya123@52.13.15.65:5439/server',
        'affiliate_mysql': 'mysql://root:papaya@aflt-mysql-slave.cjfrqij7amkp.us-west-1.rds.amazonaws.com/server'
    }


class DevConfig(Config):
    """Dev configuration."""

    pass
