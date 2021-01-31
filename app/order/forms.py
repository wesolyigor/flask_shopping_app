from datetime import datetime


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length


class OrderForm(FlaskForm):
    name = StringField('Order title', validators=[DataRequired(), Length(min=3, max=100,
                                                                         message="Tytuł musi zawierać od 3 do 100 znaków")])
    shop = SelectField('Where?', choices=['Wherever', 'Biedronka', 'Lidl', 'Other'],
                       validators=[DataRequired()])
    info = TextAreaField('Additional info:',
                         validators=[Length(max=240, message="Maksymalnie 240 znaków")])
    deadline = DateField('Deadline:', format='%Y-%m-%d',
                         validators=[DataRequired()])
    submit = SubmitField('Select Products')

    #
    # def validate_deadline(self, field):
    #     if field.data is not  datetime.strftime(field, '%Y %m %d'):
    #         raise ValidationError("Incorrect date.")
