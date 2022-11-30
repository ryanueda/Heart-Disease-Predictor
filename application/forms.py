from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, RadioField, SubmitField
from wtforms.validators import Length, InputRequired, ValidationError, NumberRange
class PredictionForm(FlaskForm):
    HighBP = RadioField("HighBP", choices=[(0, 'None'), (1, 'Yes')], validators=[InputRequired()])
    HighChol = RadioField("HighChol", choices=[(0, 'None'), (1, 'Yes')], validators=[InputRequired()])
    BMI = IntegerField("BMI", validators=[InputRequired(), NumberRange(10,50)])
    Smoker = RadioField("Smoker", choices=[(0, 'None'), (1, 'Yes')], validators=[InputRequired()])
    Stroke = RadioField("Stroke", choices=[(0, 'None'), (1, 'Yes')], validators=[InputRequired()])
    Diabetes = RadioField("Diabetes", choices=[(0, 'None'), (1, 'Yes')], validators=[InputRequired()])
    HvyAlcoholConsump = RadioField("HvyAlcoholConsump", choices=[(0, 'None'), (1, 'Yes')], validators=[InputRequired()])
    Sex = RadioField("Sex", choices=[(0, 'Female'), (1, 'Male')], validators=[InputRequired()])
    Age = IntegerField("Age", validators=[InputRequired(), NumberRange(1,100)])
    submit = SubmitField("Predict")