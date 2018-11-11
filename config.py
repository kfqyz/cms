import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 994
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kfqyz@163.com'
    MAIL_PASSWORD = 'asdf1974'
    SCHOA_MAIL_SUBJECT_PREFIX = '[SCHOA]'
    SCHOA_MAIL_SENDER = 'SCHOA Admin <kfqyz@163.com>'
    SCHOA_ADMIN = 'kfqyz@163.com'
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SCHOA_POSTS_PER_PAGE = 20
    SCHOA_FOLLOWERS_PER_PAGE = 50
    SCHOA_COMMENTS_PER_PAGE = 30
    SCHOA_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
