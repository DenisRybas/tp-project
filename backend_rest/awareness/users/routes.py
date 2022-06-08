import datetime
from functools import wraps

import jwt
from flask import current_app
from flask import url_for, Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash

from backend_rest.awareness.app import db, app
from backend_rest.awareness.models import User
from backend_rest.awareness.users.email import SmtpEmail

users_blueprint = Blueprint("users", __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers["x-access-token"]

        if not token:
            return jsonify(result="token is missing", code=403)

        try:
            jwt.decode(token, app.config["SECRET_KEY"], ["HS256"])
        except Exception as e:
            print(e)
            return jsonify(result="token is invalid", code=403)

        return f(*args, **kwargs)

    return decorated


@users_blueprint.route("/register", methods=["POST"])
def register():
    """User registration route
    ---
    post:
        parameters:
          - name: username
            in: body
            type: string
            required: true
            example: Denis
          - name: email
            in: body
            type: string
            required: true
            example: example@example.com
          - name: password
            in: body
            type: string
            required: true
            example: my_secure_password
          - name: subscribed_on_daily_phrase
            in: body
            type: boolean
            required: true
            example: 1
    responses:
      100:
        description: Registration successful
      417:
        description: User is authenticated, already exists or pending approval
      400:
        description: Invalid request method
    """
    if session.get("logged_in"):
        return jsonify(result="User is authenticated", code=417)
    if request.method == "POST":
        user_json = request.get_json(force=True)
        if User.query.filter_by(email=user_json["email"]).first() is None:
            sub = user_json["subscribed_on_daily_phrase"] == 1
            user = User(
                nickname=user_json["username"],
                email=user_json["email"],
                password=generate_password_hash(user_json["password"]),
                subscribed_on_daily_phrase=sub,
            )
            db.session.add(user)
            db.session.commit()
            send_confirm_email(user)
            return jsonify(result="Registration successful", code=100)
        else:
            return jsonify(
                result="User already exists or pending email approval", code=417
            )
    else:
        return jsonify(result="invalid request method", code=400)


@users_blueprint.route("/login", methods=["POST"])
def login():
    """User login route
    ---
    post:
        parameters:
          - name: email
            in: body
            type: string
            required: true
            example: example@example.com
          - name: password
            in: body
            type: string
            required: true
            example: my_secure_password
    responses:
      100:
        description: Login successful
      417:
        description: User is authenticated, invalid password or pending approval
      400:
        description: Invalid request method
    """
    if session.get("logged_in"):
        return jsonify(result="User is authenticated", code=417)
    if request.method == "POST":
        user_json = request.get_json()
        user = User.query.filter_by(email=user_json["email"]).first()

        if (
            user
            and user.is_confirmed
            and check_password_hash(user.password, user_json["password"])
        ):
            token = jwt.encode(
                {
                    "uid": user.id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                },
                app.config["SECRET_KEY"],
            )

            print(token)
            session["logged_in"] = True
            return jsonify(result="Login successful", token=token, code=100)
        else:
            return jsonify(result="Invalid password", code=417)
    else:
        return jsonify(result="invalid request method", code=400)


@users_blueprint.route("/edit_account", methods=["GET", "POST"])
@token_required
def edit_account():
    """User edit account route
    ---
    post:
        parameters:
          - name: username
            in: body
            type: string
            required: true
            example: Denis
          -subscribed_on_daily_phrase:
            type: boolean
            required: true
            example: 1
          - name: password
            in: body
            type: string
            required: true
            example: my_secure_password
    responses:
          100:
            description: Edit successful
          200:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    username:
                    type: string
                    example: Denis
                  subscribed_on_daily_phrase:
                    type: boolean
                    example: 1
          403:
            description: User has different email
          400:
            description: Invalid request method
    """
    user_id = User.decode_auth_token(request.headers["x-access-token"])
    user = User.query.filter_by(id=user_id).first()
    if request.method == "POST":
        user_json = request.get_json()

        user.nickname = user_json["username"]
        user.subscribed_on_daily_phrase = user_json["subscribed_on_daily_phrase"]
        if user_json["password"] != "":
            user.password = generate_password_hash(user_json["password"])
            db.session.commit()
        return jsonify(result="Account edited successfully", code=100)
    elif request.method == "GET":
        return jsonify(
            username=user.nickname,
            subscribed_on_daily_phrase=user.subscribed_on_daily_phrase,
            code=200,
        )
    else:
        return jsonify(result="invalid request method", code=400)


@users_blueprint.route("/logout")
@token_required
def logout():
    """User edit account route
    ---
    responses:
      200:
        description: Logout successful
    """
    session["logged_in"] = False
    return jsonify(result="Successful logout", code=200)


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


@users_blueprint.route("/reset_password", methods=["POST"])
def reset_request():
    """Reset password request
    ---
    post:
        parameters:
          - name: email
            in: body
            type: string
            required: true
            example: example@example.com
    responses:
      100:
        description: Password reset successful
      417:
        description: User is authenticated
      404:
        description: User not found
      400:
        description: Invalid request method
    """
    if session.get("logged_in"):
        return jsonify(result="User is authenticated", code=417)
    if request.method == "POST":
        user_json = request.get_json()
        user = User.query.filter_by(email=user_json["email"]).first()
        if user is not None:
            send_reset_email(user)
            return jsonify(result="Password reset request successful", code=100)
        else:
            return jsonify(result="User not found", code=404)
    else:
        return jsonify(result="invalid request method", code=400)


@users_blueprint.route("/reset_password/<token>", methods=["POST"])
def reset_token(token):
    """Reset password confirm
    ---
    post:
        parameters:
          - name: password
            in: body
            type: string
            required: true
            example: my_secure_password
    responses:
      100:
        description: Password updated
      417:
        description: User is authenticated
      404:
        description: User not found
      400:
        description: Invalid request method
    """
    if session.get("logged_in"):
        return jsonify(result="User is authenticated", code=417)
    user = User.verify_reset_token(token)
    if user is None:
        return jsonify(result="User not found", code=404)

    if request.method == "POST":
        user_json = request.get_json()
        user.password = generate_password_hash(user_json["password"])
        db.session.commit()
        return jsonify(result="Password updated", code=100)
    else:
        return jsonify(result="invalid request method", code=400)


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


@users_blueprint.route("/confirm_email/<token>", methods=["POST", "GET"])
def confirm_token(token):
    """User edit account route
    ---
    responses:
      100:
        description: User confirmed
      400:
        description: Invalid request method
      404:
        description: Expired or non-existing token
      417:
        description: User is authenticated
    """
    if session.get("logged_in"):
        return jsonify(result="User is authenticated", code=417)
    user = User.verify_user_token(token)
    if user is None:
        return jsonify(result="That is expired or non-existing token", code=404)
    if request.method == "POST":
        user.is_confirmed = True
        db.session.commit()
        return jsonify(result="User confirmed", code=200)
    else:
        return jsonify(result="invalid request method", code=400)
