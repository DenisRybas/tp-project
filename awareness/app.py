from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "Fatmans"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///awareness.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "noreply.fatmans.team@gmail.com"
app.config["MAIL_PASSWORD"] = "ezqgj543"

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
db = SQLAlchemy(app)
__import__("awareness.models")
# migrate = Migrate(app, db)
DATABASE_URI = getattr(app.config, "SQLALCHEMY_DATABASE_URI", "")
is_sqlite = DATABASE_URI.startswith("sqlite:")
# migrate.init_app(app, db, render_as_batch=is_sqlite)


def create_app():
    db.init_app(app)
    login_manager.init_app(app)

    from awareness.users.routes import users

    # from awareness.diaries.routes import diaries
    from awareness.main.routes import main
    from awareness.template_diaries.routes import template_diaries

    app.register_blueprint(users)
    app.register_blueprint(template_diaries)
    app.register_blueprint(main)
    return app
