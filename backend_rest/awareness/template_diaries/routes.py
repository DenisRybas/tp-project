from flask import Blueprint, request, jsonify

from backend.awareness.app import db
from backend.awareness.models import UserTemplateDiary, Theme, User
from backend.awareness.template_diaries.utils import get_random_theme_id
from backend.awareness.users.routes import token_required

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
        theme_1 = Theme.get_by_theme(diary_json['theme_1'])
        theme_2 = Theme.get_by_theme(diary_json['theme_2'])

        user_id = User.decode_auth_token(request.args.get('token'))

        diary_1 = UserTemplateDiary(user_id=int(user_id),
                                    theme_id=theme_1.id, answer=diary_json['answer_1'])
        diary_2 = UserTemplateDiary(user_id=int(user_id),
                                    theme_id=theme_2.id, answer=diary_json['answer_2'])
        db.session.add(diary_1)
        db.session.add(diary_2)
        db.session.commit()
        return jsonify("Template diary created successfully"), 100
    elif request.method == "GET":
        theme_1_id = get_random_theme_id()
        theme_2_id = get_random_theme_id()

        theme_1 = Theme.query.get(theme_1_id)
        theme_2 = Theme.query.get(theme_2_id)
        return jsonify(theme_1=theme_1, theme_2=theme_2), 200
    return None

