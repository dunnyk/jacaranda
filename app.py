"""Main package."""

from flask import Flask
from flask_migrate import Migrate
from config import AppConfig

from models.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    # bind app to db
    db.init_app(app)

    # importing the models here for all the changes
    # in the models to be detected when running the
    # migration
    # import models

    # initialize migration scripts
    Migrate(app, db)

    return app
