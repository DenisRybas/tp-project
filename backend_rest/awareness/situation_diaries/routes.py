from flask import Blueprint, request, jsonify

from backend_rest.awareness.app import db
from backend_rest.awareness.models import UserSituationDiary, Situation, User, SituationAnswer
from backend_rest.awareness.situation_diaries.utils import get_random_situation_id
from backend_rest.awareness.users.routes import token_required

situation_diaries_blueprint = Blueprint("situation_diaries", __name__)


@situation_diaries_blueprint.route("/situation_diaries/new", methods=["GET", "POST"])
@token_required
def create_situation_diary():
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
        diary_json = request.get_json(force=True)
        situation = Situation.get_by_situation(diary_json["situation"])
        chosen_answer = diary_json["answer_id"]

        user_id = User.decode_auth_token(request.args.get("token"))

        diary = UserSituationDiary(
            user_id=int(user_id), situation_id=situation.id, situation_answer_id=chosen_answer, size=2,
        )
        db.session.add(diary)
        db.session.commit()
        return jsonify("Situation diary created successfully"), 100
    elif request.method == "GET":
        situation_id = get_random_situation_id()

        situation = Situation.query.get(situation_id)
        situation_answers = SituationAnswer.query.filter_by(situation_id=situation_id)

        situation_to_json = []
        for situation_answer in situation_answers:
            situation_obj = {
                'situation': situation.situation,
                'answer': situation_answer.answer,
                'explanation': situation_answer.explanation,
                'is_preferred': situation_answer.is_preferred,
            }

            situation_to_json.append(situation_obj)

        return jsonify(situation_to_json), 200
    return None


@situation_diaries_blueprint.route("/situation_diaries/<int:situation_diary_id>", methods=["GET"])
@token_required
def get_situation_diary(situation_diary_id):
    user_id = User.decode_auth_token(request.args.get("token"))

    situation_diary = UserSituationDiary.query.filter_by(
        id=situation_diary_id, user_id=int(user_id)
    ).first_or_404()
    situation = Situation.query.get(situation_diary.situation_id)
    return jsonify(situation=situation, answer=situation_diary.answer), 200


@situation_diaries_blueprint.route("/situation_diaries", methods=["GET"])
@token_required
def get_all_situation_diaries():
    user_id = User.decode_auth_token(request.args.get("token"))

    situation_diaries = UserSituationDiary.query.filter_by(
        user_id=int(user_id)
    )

    situation_diaries_to_json = []
    for situation_diary in situation_diaries:
        situation = Situation.query.get(situation_diary.situation_id)
        diary_obj = {
            'id': situation_diary.id,
            'situation': situation
        }
        situation_diaries_to_json.append(diary_obj)

    return jsonify(situation_diaries=situation_diaries_to_json), 200
