from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length


class CreateTemplateDiaryForm(FlaskForm):
    theme_1 = HiddenField(validators=[DataRequired(), Length(max=300)])
    answer_1 = TextAreaField(
        "Your answer:", validators=[DataRequired(), Length(max=5000)]
    )
    theme_2 = HiddenField(validators=[DataRequired(), Length(max=300)])
    answer_2 = TextAreaField(
        "Your answer:", validators=[DataRequired(), Length(max=5000)]
    )
    submit = SubmitField("Finish")
