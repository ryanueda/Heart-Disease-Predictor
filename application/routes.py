from application import app
from application import ai_model
from application import db
from application.models import Entry
from datetime import datetime

#Handles http://127.0.0.1:5000/hello
@app.route('/hello')
def hello_world():
    return "<h1>Hello World</h1>"

...
from flask import render_template
from application.forms import PredictionForm
...
#Handles http://127.0.0.1:5000/
@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():
    form1 = PredictionForm()
    return render_template("index.html", form=form1, title="Enter Parameters For Prediction")

## predict route
from flask import render_template, request, flash
from application import ai_model
predict_type = ['Healthy', 'Heart Disease Or Attack']
@app.route("/predict", methods=['GET','POST'])
def predict():
    form = PredictionForm()
    if request.method == 'POST':
        if form.validate_on_submit():  
            HighBP = form.HighBP.data
            HighChol = form.HighChol.data
            BMI = form.BMI.data
            Smoker = form.Smoker.data
            Stroke = form.Stroke.data
            Diabetes = form.Diabetes.data
            HvyAlcoholConsump = form.HvyAlcoholConsump.data
            Sex = form.Sex.data
            Age = form.Age.data
            X = [[HighBP, HighChol, BMI, Smoker, Stroke, Diabetes, HvyAlcoholConsump, Sex, Age]]
            result = ai_model.predict(X)
            new_entry = Entry(HighBP=HighBP,
                              HighChol=HighChol,
                              BMI=BMI,
                              Smoker=Smoker,
                              Stroke=Stroke,
                              Diabetes=Diabetes,
                              HvyAlcoholConsump=HvyAlcoholConsump,
                              Sex=Sex,
                              Age=Age,
                              prediction=int(result[0]),
                             predicted_on=datetime.utcnow())
            add_entry(new_entry)
            
            flash(f"Prediction: {predict_type[int(result[0])]}", "success")
            return render_template("index.html", title="Enter Parameters For Prediction", form=form, index=True )
        else:
            flash("Error, cannot proceed with prediction","danger")
            return render_template("index.html", title="Enter Parameters For Prediction", form=form, index=True )

        
def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")