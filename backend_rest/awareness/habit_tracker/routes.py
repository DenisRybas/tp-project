from flask import Blueprint, request, jsonify

from backend_rest.awareness.app import db
from backend_rest.awareness.models import (
    UserSituationDiary,
    User,
    HabitTracker,
)
from backend_rest.awareness.users.routes import token_required

habit_tracker_blueprint = Blueprint("habit_tracker", __name__)


@habit_tracker_blueprint.route("/habit_tracker/new", methods=["POST"])
@token_required
def create_habit():
    """Create situation diary route
    ---
    post:
        parameters:
          - name: situation_1
            in: body
            type: string
            required: true
            example: Is life good?
          - name: situation_2
            in: body
            type: string
            required: true
            example: What good did you do today?
          - name: answer_1
            in: body
            type: string
            required: true
            example: Yes
          - name: answer_2
            in: body
            type: string
            required: true
            example: Nothing
    responses:
      100:
        description: Situation diary successfully created
      200:
        content:
        application/json:
          schema:
            type: object
            properties:
              situation_1:
                type: string
                example: Is life good?
              situation_2:
                type: string
                example: What good did you do today?
    """
    if request.method == "POST":
        habit_json = request.get_json(force=True)
        habit_name = habit_json["habit_name"]

        token = request.headers["x-access-token"]
        user_id = User.decode_auth_token(token)

        habit_tracker = HabitTracker(
            user_id=int(user_id),
            habit_name=habit_name,
        )
        db.session.add(habit_tracker)
        db.session.commit()
        return jsonify(result="Habit tracker created successfully", code=100)
    return None


@habit_tracker_blueprint.route("/habit_tracker/<int:habit_id>", methods=["GET"])
@token_required
def get_habit_tracker(habit_id):
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    habit = HabitTracker.query.filter_by(id=habit_id, user_id=user_id).first()

    return jsonify(
        habit_name=habit.habit_name,
        date_started=habit.date_started,
        code=200,
    )


@habit_tracker_blueprint.route("/habit_trackers", methods=["GET"])
@token_required
def get_all_habit_trackers():
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    habit_query = UserSituationDiary.query.filter_by(user_id=int(user_id))

    habits = []
    for habit in habit_query:
        habits.append(
            {
                "habit_id": habit.id,
                "habit_name": habit.habit_name,
                "date_started": habit.date_started,
            }
        )

    return jsonify(habits=habits, code=200)
