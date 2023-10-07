from decouple import config


class Config:
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', default='')
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
    DEBUG = config('DEBUG', default=False, cast=bool)
