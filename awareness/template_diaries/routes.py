from flask import render_template, url_for, flash, redirect, Blueprint, request, abort
from flask_login import login_required, current_user

from awareness.app import db
from awareness.models import UserTemplateDiary, Theme
from awareness.template_diaries.forms import CreateTemplateDiaryForm
from awareness.template_diaries.utils import get_random_theme_id

template_diaries = Blueprint("template_diaries", __name__)


@template_diaries.route("/template_diaries/new", methods=["GET", "POST"])
@login_required
def create_template_diary():
    form = CreateTemplateDiaryForm()
    if form.validate_on_submit():
        theme_1 = Theme.get_by_theme(form.theme_1.data)
        theme_2 = Theme.get_by_theme(form.theme_2.data)

        diary_1 = UserTemplateDiary(user_id=int(current_user.get_id()), theme_id=theme_1.id, answer=form.answer_1.data)
        diary_2 = UserTemplateDiary(user_id=int(current_user.get_id()), theme_id=theme_2.id, answer=form.answer_2.data)
        db.session.add(diary_1)
        db.session.add(diary_2)
        db.session.commit()
        return redirect(url_for('main.index'))
    elif request.method == "GET":
        theme_1_id = get_random_theme_id()
        theme_2_id = get_random_theme_id()

        theme_1 = Theme.query.get(theme_1_id)
        theme_2 = Theme.query.get(theme_2_id)

        form.theme_1.data = theme_1.theme
        form.theme_2.data = theme_2.theme
    return render_template('template_diary.html', title='New template diary',
                           form=form)


@template_diaries.route("/template_diaries/<int:template_diary_id>", methods=["GET"])
@login_required
def get_template_diary(template_diary_id):
    template_diary = UserTemplateDiary.query\
        .filter_by(id=template_diary_id, user_id=int(current_user.get_id())).first_or_404()
    return render_template("template_diary.html", template_diary=template_diary)


@template_diaries.route("/template_diaries", methods=["GET"])
@login_required
def get_all_template_diaries():
    template_diary = UserTemplateDiary.query\
        .filter_by(user_id=int(current_user.get_id())).first_or_404()
    return render_template("template_diaries.html", template_diary=template_diary)
