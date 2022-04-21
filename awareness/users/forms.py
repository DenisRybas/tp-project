from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Regexp

from awareness.models import User


class RegistrationForm(FlaskForm):
    nickname = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(
        "Email", validators=[DataRequired(), Regexp("[^@]+@[^@]+\.[^@]+")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    subscribed_on_daily_phrase = BooleanField("Subscribe on daily phrase")
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(nickname=username.data).first()
        if user:
            raise ValidationError(
                "That username is taken. Please choose a different one."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one.")


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Regexp("[^@]+@[^@]+\.[^@]+")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class UpdateAccountForm(FlaskForm):
    nickname = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    password = PasswordField("Password")
    confirm_password = PasswordField(
        "Confirm Password", validators=[EqualTo("password")]
    )
    subscribed_on_daily_phrase = BooleanField("Subscribe on daily phrase")
    submit = SubmitField("Update")

    def validate_nickname(self, nickname):
        if nickname.data != current_user.nickname:
            user = User.query.filter_by(nickname=nickname.data).first()
            if user:
                raise ValidationError(
                    "That username is taken. Please choose a different one."
                )


class RequestResetForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Regexp("[^@]+@[^@]+\.[^@]+")]
    )
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. You must register first."
            )


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset Password")


class ConfirmEmailForm(FlaskForm):
    submit = SubmitField("Confirm your account")
