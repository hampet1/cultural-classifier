import os
import pickle


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    DEBUG = False
    TESTING = False
    DB_NAME = "database.db"
    # path to our ML model
    PATH_MODEL = os.getcwd().replace("\\", "/") + "/cultural_classifier.pkl"
    # unpickling (deserializing)
    MODEL = pickle.load(open(PATH_MODEL, 'rb'))


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    TESTING = True


config = {
    "default": "main.config.BaseConfig",
    "development": "main.config.DevelopmentConfig",
    "production": "main.config.ProductionConfig",
    "testing": "main.config.TestingConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_ENV')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('application.cfg', silent=True)
