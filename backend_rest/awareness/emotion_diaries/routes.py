from datetime import datetime

from flask import Blueprint, request, jsonify

# from awareness.users.routes import token_required
from awareness.app import db
from awareness.models import UserEmotion, Emotion, Action, User
from awareness.users.routes import token_required

emotion_diaries_blueprint = Blueprint("emotion_diaries", __name__)


@emotion_diaries_blueprint.route("/emotion_diaries/new", methods=["GET", "POST"])
@token_required
def create_emotion_diary():
    """Create emotion diary route
    ---
    post:
        parameters:
          - name: emotion_1
            in: body
            type: string
            required: true
            example: Is life good?
          - name: emotion_2
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
        description: Emotion diary successfully created
      200:
        content:
        application/json:
          schema:
            type: object
            properties:
              emotion_1:
                type: string
                example: Is life good?
              emotion_2:
                type: string
                example: What good did you do today?
    """
    if request.method == "POST":
        diary_json = request.get_json(force=True)
        emotion_list_json = diary_json["emotions"]
        action_list_json = diary_json["actions"]
        day_rate = int(diary_json["day_rate"])

        token = request.headers["x-access-token"]
        user_id = User.decode_auth_token(token)

        for emotion in emotion_list_json:
            for action in action_list_json:
                diary = UserEmotion(
                    user_id=int(user_id),
                    emotion_id=int(emotion),
                    action_id=int(action),
                    day_rate=int(day_rate),
                )
                db.session.add(diary)
                db.session.commit()

        return jsonify(result="Emotion diary created successfully", code=100)
    elif request.method == "GET":
        emotions = Emotion.query.all()
        actions = Action.query.all()

        emotions_to_json = []
        for emotion in emotions:
            emotion_obj = {"emotion_id": emotion.id, "emotion": emotion.emotion_name}

            emotions_to_json.append(emotion_obj)

        actions_to_json = []
        for action in actions:
            action_obj = {"action_id": action.id, "action": action.action_name}

            actions_to_json.append(action_obj)

        return jsonify(emotions=emotions_to_json, actions=actions_to_json, code=200)
    return None


@emotion_diaries_blueprint.route(
    "/emotion_diaries/<int:emotion_diary_id>", methods=["GET"]
)
@token_required
def get_emotion_diary(emotion_diary_id):
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    emotion_diary = UserEmotion.query.filter_by(
        id=emotion_diary_id, user_id=user_id
    ).first_or_404()

    # splitted_date = emotion_diary.date.strftime("%Y")

    year = int(emotion_diary.date.year)
    month = int(emotion_diary.date.month)
    day = int(emotion_diary.date.day)

    start = datetime(year, month, day, 0, 0, 0, 0)
    end = datetime(year, month, day, 23, 59, 59, 9999)

    emotions_actions = UserEmotion.query.filter(UserEmotion.date <= end).filter(
        UserEmotion.date >= start
    )

    emotions_to_json = []
    for emotion_action in emotions_actions:
        emotions_to_json.append(
            Emotion.query.get(emotion_action.emotion_id).emotion_name
        )

    actions_to_json = []
    for emotion_action in emotions_actions:
        actions_to_json.append(Action.query.get(emotion_action.action_id).action_name)

    return jsonify(
        date=str(day) + "." + str(month) + "." + str(year),
        emotions=emotions_to_json,
        actions=actions_to_json,
        day_rate=emotion_diary.day_rate,
        code=200,
    )


@emotion_diaries_blueprint.route("/emotion_diaries", methods=["GET"])
@token_required
def get_all_emotion_diaries():
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    emotion_diaries = UserEmotion.query.filter_by(user_id=int(user_id))

    emotion_diaries_to_json = []
    for emotion_diary in emotion_diaries:
        year = str(emotion_diary.date.year)
        month = str(emotion_diary.date.month)
        day = str(emotion_diary.date.day)
        diary_obj = {"id": emotion_diary.id, "date": year + "." + month + "." + day}
        emotion_diaries_to_json.append(diary_obj)

    return jsonify(emotion_diaries=emotion_diaries_to_json, code=200)
