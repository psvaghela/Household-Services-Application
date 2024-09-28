class Config(object):
    debug = False
    testing = False


class DevelopmentConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
