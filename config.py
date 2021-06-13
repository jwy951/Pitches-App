import os
# from flask import app

class Config:
    """
    General configuration parent class
    """
    #pass
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
#     if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#         SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
#     pass

class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    pass
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


# class DevConfig(Config):
#     '''
#     Development  configuration child class
#     '''
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:30196642@localhost/yegon'
#     '''
#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True


class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}