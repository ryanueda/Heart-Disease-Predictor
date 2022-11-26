from application import app
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
    return render_template("index.html", form=form1, title="Enter Iris Parameters")

## predict route
from flask import render_template, request, flash
@app.route("/predict", methods=['GET','POST'])
def predict():
    form = PredictionForm()
    if request.method == 'POST':
        if form.validate_on_submit():  
            sepal_l = form.sepal_l.data
            sepal_w = form.sepal_w.data
            petal_l = form.petal_l.data
            petal_w = form.petal_w.data
            flash(f"Prediction: ","success")
        else:
            flash("Error, cannot proceed with prediction","danger")
            return render_template("index.html", title="Enter Iris Parameters", form=form, index=True )