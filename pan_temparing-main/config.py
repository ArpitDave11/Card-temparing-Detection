import os
from os import environ


class Config(object):
    DEBUG = False
    TESTING = False

    # Obtaining the absolute path of the directory containing the current file
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY= "Daveroot@007"
    DB_NAME= "production-db"
    DB_USERNAME="root"
    DB_PASSWORD="Daveroot@007"
    # adding uploading path.
    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE = False
    DEFAULT_THEME = None


class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    TESTING = False

    # Obtaining the absolute path of the directory containing the current file
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY= "Daveroot@007"
    DB_NAME= "production-db"
    DB_USERNAME="root"
    DB_PASSWORD="Daveroot@007"

class Testing(Config):
    DEBUG = False
    TESTING = True

    # Obtaining the absolute path of the directory containing the current file
    basedir = os.path.abspath (os.path.dirname (__file__))

    SECRET_KEY= "Daveroot@007"
    DB_NAME= "production-db"
    DB_USERNAME="root"
    DB_PASSWORD="Daveroot@007"

class Testing(Config):
    DEBUG= False





