import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CMS_MAIL_SUBJECT_PREFIX = '[CMS]'
    CMS_MAIL_SENDER = 'kfqyz@sina.com'
    CMS_ADMIN = os.environ.get('CMS_ADMIN')
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    CMS_POSTS_PER_PAGE = 10
    CMS_FOLLOWERS_PER_PAGE = 20
    CMS_COMMENTS_PER_PAGE = 15
    CMS_SLOW_DB_QUERY_TIME = 0.5

    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_PKG_TYPE = 'full'  # basic, standard and full.
    CKEDITOR_HEIGHT = 400
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_FILE_UPLOADER = 'blog.upload'
    # CKEDITOR_ENABLE_CSRF = True  # if you want to enable CSRF protect, uncomment this line
    UPLOADED_PATH = os.path.join(basedir, 'app\\static\\uploads')
    BLOG_PIC_PATH = os.path.join(UPLOADED_PATH, 'blog_pic')
    AVATARS_SAVE_PATH = os.path.join(UPLOADED_PATH, 'avatars')
    AVATARS_SIZE_TUPLE = (30, 100, 200)  # default:(30.60.150)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/cms?charset=utf8'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/cms?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
