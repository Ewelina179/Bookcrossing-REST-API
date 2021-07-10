from db import db

class CityModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    shelf = db.relationship("ShelfModel", lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'shelfs': [shelf.json() for shelf in self.shelf.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    """
    def find_all(self):
        cities = CityModel.query.all()
        return {'name' : [self.name for self.name in cities]}
    """

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
