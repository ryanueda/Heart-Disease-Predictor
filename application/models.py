from application import db
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    HighBP = db.Column(db.Float)
    HighChol = db.Column(db.Float)
    BMI = db.Column(db.Float)
    Smoker = db.Column(db.Float)
    Stroke = db.Column(db.Float)
    Diabetes = db.Column(db.Float)
    HvyAlcoholConsump = db.Column(db.Float)
    Sex = db.Column(db.Float)
    Age = db.Column(db.Float)
    prediction = db.Column(db.Integer)
    predicted_on = db.Column(db.DateTime, nullable=False)