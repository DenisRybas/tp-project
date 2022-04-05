from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# app.config.from_pyfile('babel.cfg')
babel = Babel(app)
back_uri = "app/backend/app/"
