from flask import Flask
from app import flask_config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(flask_config.get_flask_config())
db = SQLAlchemy(app)

from app import routes, db
