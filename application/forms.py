from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import Length, InputRequired, ValidationError, NumberRange
class PredictionForm(FlaskForm):
    HighBP = FloatField("HighBP", validators=[InputRequired(), NumberRange(0,1)])
    HighChol = FloatField("HighChol", validators=[InputRequired(), NumberRange(0,1)])
    BMI = FloatField("BMI", validators=[InputRequired(), NumberRange(0,50)])
    Smoker = FloatField("Smoker", validators=[InputRequired(), NumberRange(0,1)])
    Stroke = FloatField("Stroke", validators=[InputRequired(), NumberRange(0,1)])
    Diabetes = FloatField("Diabetes", validators=[InputRequired(), NumberRange(0,1)])
    HvyAlcoholConsump = FloatField("HvyAlcoholConsump", validators=[InputRequired(), NumberRange(0,1)])
    Sex = FloatField("Sex", validators=[InputRequired(), NumberRange(0,1)])
    Age = FloatField("Age", validators=[InputRequired(), NumberRange(0,100)])
    submit = SubmitField("Predict")