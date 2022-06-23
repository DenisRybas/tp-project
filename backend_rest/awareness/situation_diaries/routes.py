from flask import Blueprint, request, jsonify

from awareness.app import db
from awareness.models import (
    UserSituationDiary,
    Situation,
    User,
    SituationAnswer,
)
from awareness.situation_diaries.utils import get_random_situation_id
from awareness.users.routes import token_required


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
        chosen_answer = diary_json["answer"]

        token = request.headers["x-access-token"]
        user_id = User.decode_auth_token(token)

        situation_answer = SituationAnswer.query.filter_by(
            situation_id=situation.id, answer=chosen_answer
        ).first()

        diary = UserSituationDiary(
            user_id=int(user_id),
            situation_id=situation.id,
            situation_answer_id=situation_answer.id,
            size=2,
        )
        db.session.add(diary)
        db.session.commit()
        return jsonify(result="Situation diary created successfully", code=100)
    elif request.method == "GET":
        situation_id = get_random_situation_id()

        situation = Situation.query.get(situation_id)
        situation_answers = SituationAnswer.query.filter_by(situation_id=situation_id)

        situation_to_json = []
        preferred_answer = ""
        for situation_answer in situation_answers:
            if situation_answer.is_preferred:
                preferred_answer = situation_answer.answer
            situation_obj = {
                "situation": situation.situation,
                "answer": situation_answer.answer,
                "explanation": situation_answer.explanation,
                "is_preferred": situation_answer.is_preferred,
            }

            situation_to_json.append(situation_obj)

        return jsonify(
            situation=situation_to_json, preferred_answer=preferred_answer, situation_name=situation.situation, code=200
        )
    return None


@situation_diaries_blueprint.route(
    "/situation_diaries/<int:situation_diary_id>", methods=["GET"]
)
@token_required
def get_situation_diary(situation_diary_id):
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    situation_diary = UserSituationDiary.query.filter_by(
        id=situation_diary_id, user_id=int(user_id)
    ).first_or_404()
    situation = Situation.query.get(situation_diary.situation_id)
    situation_answer_list = SituationAnswer.query.filter_by(
        situation_id=situation_diary.situation_id
    )
    situation_answer_list_to_json = []
    preferred_answer = ""
    user_answer = ""
    for situation_answer in situation_answer_list:
        if situation_answer.is_preferred:
            preferred_answer = situation_answer.answer
        if situation_answer.id == situation_diary.situation_answer_id:
            user_answer = situation_answer.answer
        situation_answer_list_to_json.append(
            {
                "answer": situation_answer.answer,
                "explanation": situation_answer.explanation,
            }
        )
    return jsonify(
        situation=situation.situation,
        answers=situation_answer_list_to_json,
        preferred_answer=preferred_answer,
        user_answer=user_answer,
        code=200,
    )


@situation_diaries_blueprint.route("/situation_diaries", methods=["GET"])
@token_required
def get_all_situation_diaries():
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    situation_diaries = UserSituationDiary.query.filter_by(user_id=int(user_id))

    situation_diaries_to_json = []
    for situation_diary in situation_diaries:
        situation = Situation.query.get(situation_diary.situation_id)
        diary_obj = {"id": situation_diary.id, "situation": situation.situation}
        situation_diaries_to_json.append(diary_obj)

    return jsonify(situation_diaries=situation_diaries_to_json, code=200)
