from db import db

class ShellModel(db.Model):
    
    __tablename_ = 'shells'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    adress = db.Column(db.String(128))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    #book = db.relationship("BookModel", lazy='dynamic')

    #relacja z książką - czy backref dobrze napisane? nazwa tabeli czy klasa?