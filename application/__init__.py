from flask import Flask
import joblib
from flask_sqlalchemy import SQLAlchemy
import pickle

#create the Flask app
app = Flask(__name__)

# load configuration from config.cfg
app.config.from_pyfile('config.cfg')
## instantiate SQLAlchemy to handle db process
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# new method for SQLAlchemy version 3 onwards
with app.app_context():
    db.init_app(app)
    from .models import Entry
    db.create_all()
    db.session.commit()
    print('Created Database!')

joblib_file = './application/static/joblib_Model.pkl'
with open(joblib_file, 'rb') as f:
    ai_model = pickle.load(f)


#run the file routes.py
from application import routes