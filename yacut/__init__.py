from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config
from yacut.queries import MyQuery


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app, query_class=MyQuery)
migrate = Migrate(app, db)

from yacut import api_views, error_handlers, views