import os

from flask import Flask

from database.models.setting import Session

def make_flask_app(name):

    app = Flask(name)

    config_type = {
        "development":  "config.Development",
        "testing": "config.Testing",
    }

    app.config.from_object(config_type.get(os.getenv('FLASK_APP_ENV', 'development')))

    return app

def before_request():

    pass


def after_request(response):

    Session.remove()

    return response

def set_logger(app):

    logger = app.logger

    logger.setLevel(app.config.get('LOG_LEVEL'))
