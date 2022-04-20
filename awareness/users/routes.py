from flask import render_template, url_for, flash, redirect, Blueprint, request, abort
from sqlalchemy import or_

from awareness.users.email import SmtpEmail
from awareness.users.forms import (
    RegistrationForm,
    LoginForm,
    UpdateAccountForm,
    RequestResetForm,
    ResetPasswordForm,
    ConfirmEmailForm,
)
from awareness.models import User, load_user
from flask_login import login_user, current_user, login_required, logout_user
from awareness.app import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            nickname=form.nickname.data,
            email=form.email.data,
            password=hashed_password,
            is_confirmed=False,
            subscribed_on_daily_phrase=form.subscribed_on_daily_phrase.data,
        )
        db.session.add(user)
        db.session.commit()
        send_confirm_email(user)
        flash(
            "An email has been sent with instructions to confirm your account.", "info"
        )
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in!", "success")
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if (
            user
            and check_password_hash(user.password, form.password.data)
            and user.is_confirmed
        ):
            login_user(user, remember=form.remember.data)
            flash("You have been logged in!", "success")
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.index"))
        else:
            flash("Login unsuccessful. Please check your data", "danger")
    return render_template("login.html", title="Sign In", form=form)


@users.route("/edit_account/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_account(user_id):
    form = UpdateAccountForm()
    user = User.query.get_or_404(user_id)
    if user_id == current_user.id:
        if form.validate_on_submit():
            user.nickname = form.nickname.data
            user.subscribed_on_daily_phrase = form.subscribed_on_daily_phrase
            if form.password.data != "":
                user.password = generate_password_hash(form.nickname.data)
            db.session.commit()
            flash("Your account has been updated!", "success")
            return redirect(url_for("users.edit_account", user_id=user.id))
        elif request.method == "GET":
            form.nickname.data = user.nickname
            form.password.data = user.password
            form.subscribed_on_daily_phrase = user.subscribed_on_daily_phrase
        return render_template(
            "edit_account.html", title="Account", form=form, user=user
        )
    else:
        abort(403)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


def send_reset_email(user):
    token = user.get_user_token()
    email = SmtpEmail(
        login=current_app.config["MAIL_USERNAME"],
        password=current_app.config["MAIL_PASSWORD"],
    )
    email.send(
        to=user.email,
        message=f"""To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
""",
    )


@users.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(
            "An email has been sent with instructions to reset your password.", "info"
        )
        return redirect(url_for("users.login"))
    return render_template("reset_request.html", title="Reset Password", form=form)


@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    user = User.verify_user_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("users.reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You are now able to log in", "success")
        return redirect(url_for("users.login"))
    return render_template("reset_token.html", title="Reset Password", form=form)


def send_confirm_email(user):
    token = user.get_user_token()
    email = SmtpEmail(
        login=current_app.config["MAIL_USERNAME"],
        password=current_app.config["MAIL_PASSWORD"],
    )
    email.send(
        message=f"""To confirm your account, visit the following link:
            {url_for('users.confirm_token', token=token, _external=True)}
            If you did not make this request then simply ignore this email and no changes will be made.
            """,
        to=user.email,
    )


@users.route("/confirm_email/<token>", methods=["POST", "GET"])
def confirm_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    user = User.verify_user_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("users.register"))
    form = ConfirmEmailForm()
    if form.validate_on_submit():
        user.is_confirmed = True
        db.session.commit()
        flash("Your email is confirmed! You are now able to sign in", "success")
        return redirect(url_for("users.login"))
    return render_template("confirm_token.html", title="Confirm user", form=form)
