from datetime import datetime

import jwt
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import types

from awareness.app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(100), nullable=False)
    user_role = db.Column(db.Integer, db.ForeignKey("user_role.id"), default=2)
    subscribed_on_daily_phrase = db.Column(db.Boolean, nullable=False, default=False)

    related_diaries = db.relationship(
        "UserTemplateDiary", backref="related_template_diary", lazy=True
    )
    related_daily_phrases = db.relationship(
        "UserDailyPhrase", backref="related_daily_phrases", lazy=True
    )
    related_habits = db.relationship(
        "HabitTracker", backref="related_habits", lazy=True
    )
    related_emotions = db.relationship(
        "UserEmotion", backref="related_emotions", lazy=True
    )
    related_situations = db.relationship(
        "UserSituationDiary", backref="related_situation_diaries", lazy=True
    )
    related_technical_support_tickets = db.relationship(
        "TechnicalSupportTicket", backref="related_technical_support_tickets", lazy=True
    )
    related_technical_support_chats = db.relationship(
        "TechnicalSupportChat", backref="related_technical_support_messages", lazy=True
    )

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get("SECRET_KEY"), ["HS256"])
            return payload["uid"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."

    def get_user_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_user_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            print(s.loads(token))
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return self.name + " " + self.surname


class UserType(types.TypeDecorator):
    impl = types.String

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(UserType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.items() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class UserRole(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    role = db.Column(
        UserType({"TechnicalSupport": "TechnicalSupport", "CommonUser": "CommonUser"}),
        nullable=False,
    )
    related_users = db.relationship("User", backref="related_user_role", lazy=True)


class Theme(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    theme = db.Column(db.String(150), nullable=False, unique=True)
    related_diaries = db.relationship(
        "UserTemplateDiary", backref="related_user_template_diary", lazy=True
    )

    @staticmethod
    def get_by_theme(theme):
        return Theme.query.filter_by(theme=theme).first()


class UserTemplateDiary(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    theme_id = db.Column(db.Integer, db.ForeignKey("theme.id"), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    size = db.Column(db.Integer, nullable=False, default=2)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class DailyPhrase(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    phrase = db.Column(db.String(200), nullable=False)
    related_users = db.relationship(
        "UserDailyPhrase", backref="related_users", lazy=True
    )


class UserDailyPhrase(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    phrase_id = db.Column(db.Integer, db.ForeignKey("daily_phrase.id"), nullable=False)


class FAQData(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    question = db.Column(db.String(150), nullable=False)
    answer = db.Column(db.String(500), nullable=False)


class HabitTracker(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    habit_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date_started = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Emotion(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    emotion_name = db.Column(db.String(100), nullable=False)
    related_users = db.relationship("UserEmotion", backref="related_users", lazy=True)


class Action(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    action_name = db.Column(db.String(100), nullable=False)
    related_users = db.relationship(
        "UserEmotion", backref="related_user_actions", lazy=True
    )


class UserEmotion(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    emotion_id = db.Column(db.Integer, db.ForeignKey("emotion.id"), nullable=False)
    action_id = db.Column(db.Integer, db.ForeignKey("action.id"), nullable=False)
    day_rate = db.Column(db.SmallInteger, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class SituationAnswer(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    situation_id = db.Column(db.Integer, db.ForeignKey("situation.id"), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    explanation = db.Column(db.String(200), nullable=False)
    is_preferred = db.Column(db.Boolean, nullable=False, default=False)


class Situation(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    situation = db.Column(db.String(200), nullable=False)
    related_situation_answer = db.relationship(
        "SituationAnswer", backref="related_situation_answers", lazy=True
    )
    related_situation_diary = db.relationship(
        "UserSituationDiary", backref="related_situation_diary", lazy=True
    )

    @staticmethod
    def get_by_situation(situation):
        return Situation.query.filter_by(situation=situation).first()


class UserSituationDiary(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    situation_id = db.Column(db.Integer, db.ForeignKey("situation.id"), nullable=False)
    situation_answer_id = db.Column(
        db.Integer, db.ForeignKey("situation_answer.id"), nullable=False
    )
    size = db.Column(db.Integer, nullable=False, default=2)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class TechnicalSupportTicket(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.String(700), nullable=False)
    is_resolved = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    related_technical_support_chats = db.relationship(
        "TechnicalSupportChat", backref="related_technical_support_chats", lazy=True
    )


class TechnicalSupportChat(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    ticket_id = db.Column(
        db.Integer, db.ForeignKey("technical_support_ticket.id"), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
