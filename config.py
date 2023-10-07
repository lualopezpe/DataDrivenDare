import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///DataDrivenDare.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'data/'
