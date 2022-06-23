from flask import Blueprint, request, jsonify

from awareness.app import db
from awareness.models import UserTemplateDiary, Theme, User
from awareness.template_diaries.utils import get_random_theme_id
from awareness.users.routes import token_required

template_diaries_blueprint = Blueprint("template_diaries", __name__)


@template_diaries_blueprint.route("/template_diaries/new", methods=["GET", "POST"])
@token_required
def create_template_diary():
    """Create template diary route
    ---
    post:
        parameters:
          - name: theme_1
            in: body
            type: string
            required: true
            example: Is life good?
          - name: theme_2
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
        description: Template diary successfully created
      200:
        content:
        application/json:
          schema:
            type: object
            properties:
              theme_1:
                type: string
                example: Is life good?
              theme_2:
                type: string
                example: What good did you do today?
    """
    if request.method == "POST":
        diary_json = request.get_json(force=True)
        theme = Theme.get_by_theme(diary_json["theme"])

        token = request.headers["x-access-token"]
        user_id = User.decode_auth_token(token)

        diary = UserTemplateDiary(
            user_id=int(user_id), theme_id=theme.id, answer=diary_json["answer"]
        )
        db.session.add(diary)
        db.session.commit()
        return jsonify(result="Template diary created successfully", code=100)
    elif request.method == "GET":
        theme_id = get_random_theme_id()

        theme = Theme.query.get(theme_id)
        return jsonify(theme=theme.theme, code=200)
    return None


@template_diaries_blueprint.route(
    "/template_diaries/<int:template_diary_id>", methods=["GET"]
)
@token_required
def get_template_diary(template_diary_id):
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    template_diary = UserTemplateDiary.query.filter_by(
        id=template_diary_id, user_id=int(user_id)
    ).first_or_404()
    theme = Theme.query.get(template_diary.theme_id)
    return jsonify(theme=theme.theme, answer=template_diary.answer, code=200)


@template_diaries_blueprint.route("/template_diaries", methods=["GET"])
@token_required
def get_all_template_diaries():
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    template_diaries = UserTemplateDiary.query.filter_by(user_id=int(user_id))

    template_diaries_to_json = []
    for template_diary in template_diaries:
        theme = Theme.query.get(template_diary.theme_id)
        diary_obj = {
            "id": template_diary.id,
            "theme": theme.theme,
            "date_created": template_diary.date_created,
        }
        template_diaries_to_json.append(diary_obj)

    return jsonify(template_diaries=template_diaries_to_json, code=200)
