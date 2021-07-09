from db import db

class CityModels(db.Models):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    #nie wiem, czy jeszcze jakaś metoda
