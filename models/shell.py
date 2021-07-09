from flask.app import Flask
from db import db

class ShellModel(db.Model):
    
    __tablename_ = 'shells'
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String(128))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    book = db.relationship('Book', backref='shells', lazy=True)
    #relacja z książką - czy backref dobrze napisane? nazwa tabeli czy klasa?