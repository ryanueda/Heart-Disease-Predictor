from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import Length, InputRequired, ValidationError, NumberRange
class PredictionForm(FlaskForm):
    sepal_l = FloatField("Sepal Length", validators=[InputRequired(), NumberRange(0,10)])
    sepal_w = FloatField("Sepal Width", validators=[InputRequired(), NumberRange(0,10)])
    petal_l = FloatField("Petal Length", validators=[InputRequired(), NumberRange(0,10)])
    petal_w = FloatField("Petal Width", validators=[InputRequired(), NumberRange(0,10)])
    submit = SubmitField("Predict")