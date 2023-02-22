from application import app
from application import ai_model
from application import db
from application.models import Entry
from datetime import datetime

#Handles http://127.0.0.1:5000/hello
@app.route('/hello')
def hello_world():
    return "<h1>Hello World</h1>"

from flask import render_template
from application.forms import PredictionForm

#Handles http://127.0.0.1:5000/
@app.route('/index')
@app.route('/predict')
def index_page():
    form1 = PredictionForm()
    return render_template("index.html", form=form1, entries=get_entries(), predict_type=predict_type, title="yan's personality test")

## home page
@app.route('/home')
def home_page():
    return render_template("home.html", entries=get_entries(), predict_type=predict_type, title="Home Page")

## predict route
from flask import render_template, request, flash
from application import ai_model
predict_type = ['Healthy', 'Heart Disease Or Attack']
@app.route("/predict", methods=['GET','POST'])
def predict():
    form = PredictionForm()
    if request.method == 'POST':
        if form.validate_on_submit():  
            Qn1 = form.Qn1.data
            Qn2 = form.Qn2.data
            Qn3 = form.Qn3.data
            Qn4 = form.Qn4.data
            Qn5 = form.Qn5.data
            Qn6 = form.Qn6.data
            Qn7 = form.Qn7.data
            Qn8 = form.Qn8.data
            Qn9 = form.Qn9.data
            Qn10 = form.Qn10.data
            X = [[Qn1, Qn2, Qn3, Qn4, Qn5, Qn6, Qn7, Qn8, Qn9, Qn10]]
            result = ai_model.predict(X)
            new_entry = Entry(Qn1=Qn1, 
                            Qn2=Qn2,
                            Qn3=Qn3,
                            Qn4=Qn4,
                            Qn5=Qn5,
                            Qn6=Qn6,
                            Qn7=Qn7,
                            Qn8=Qn8,
                            Qn9=Qn9,
                            Qn10=Qn10,
                            prediction=int(result[0]),
                            predicted_on=datetime.utcnow())
            add_entry(new_entry)
            
            flash(f"Prediction: {predict_type[int(result[0])]}", "success")
            return render_template("index.html", title="yan's personality test", form=form, index=True, entries=get_entries(), predict_type=predict_type )
        else:
            flash("Error, cannot proceed with prediction","danger")
            return render_template("index.html", title="yan's personality test", form=form, index=True )

@app.route('/remove', methods=['POST'])
def remove():
    form = PredictionForm()
    req = request.form
    id = req["id"]
    remove_entry(id)
    return render_template("index.html", title="Enter Iris Parameters",
    form=form, entries = get_entries(), index=True, predict_type=predict_type)


#API get entry
@app.route("/api/get/<id>", methods=['GET'])
def api_get(id):
    #retrieve the entry using id from client
    entry = get_entry(int(id))
    #Prepare a dictionary for json conversion
    data = {
        'id' : entry.id,
        'Qn1' : entry.Qn1,
        'Qn2' : entry.Qn2,
        'Qn3' : entry.Qn3,
        'Qn4' : entry.Qn4,
        'Qn5' : entry.Qn5,
        'Qn6' : entry.Qn6,
        'Qn7' : entry.Qn7,
        'Qn8' : entry.Qn8,
        'Qn9' : entry.Qn9,
        'Qn10': entry.Qn10,
        'prediction': entry.prediction}
    #Convert the data to json
    result = jsonify(data)
    return result #response back

        
def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")

def get_entries():
    try:
        # entries = Entry.query.all() # version 2
        entries = db.session.execute(db.select(Entry).order_by(Entry.id)).scalars()
        return entries
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

# Added in Practical 5
def remove_entry(id):
    try:
        # entry = Entry.query.get(id) # version 2
        entry = db.get_or_404(Entry, id)
        db.session.delete(entry)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

from flask import json, jsonify
...
#API: add entry
@app.route("/api/add", methods=['POST'])
def api_add():
    #retrieve the json file posted from client
    data = request.get_json()
    #retrieve each field from the data
    Qn1 = data['Qn1']
    Qn2 = data['Qn2']
    Qn3 = data['Qn3']
    Qn4 = data['Qn4']
    Qn5 = data['Qn5']
    Qn6 = data['Qn6']
    Qn7 = data['Qn7']
    Qn8 = data['Qn8']
    Qn9 = data['Qn9']
    Qn10 = data['Qn10']
    prediction = data['prediction']
    #create an Entry object store all data for db action
    new_entry = Entry(
        Qn1=Qn1, 
        Qn2=Qn2,
        Qn3=Qn3,
        Qn4=Qn4,
        Qn5=Qn5,
        Qn6=Qn6,
        Qn7=Qn7,
        Qn8=Qn8,
        Qn9=Qn9,
        Qn10=Qn10,
        prediction = prediction,
        predicted_on=datetime.utcnow())
    #invoke the add entry function to add entry
    result = add_entry(new_entry)
    #return the result of the db action
    return jsonify({'id':result})

def get_entry(id):
    try:
        # entries = Entry.query.filter(Entry.id==id) version 2
        result = db.get_or_404(Entry, id)
        return result
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

#API delete entry
@app.route("/api/delete/<id>", methods=['GET'])
def api_delete(id):
    entry = remove_entry(int(id))
    return jsonify({'result':'ok'})

## route to handle login page
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Try Again.'
            flash(error, "danger")
            return render_template("login.html", title="Login Page", error=error)
        else:
            return render_template("home.html", entries=get_entries(), predict_type=predict_type, title="Home Page")

    return render_template("login.html", title="Login Page", error=error)

@app.route('/history')
def history_page():
    return render_template("history.html", entries=get_entries(), predict_type=predict_type, title="History Page")