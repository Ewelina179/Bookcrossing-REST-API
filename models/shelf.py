from db import db

class ShelfModel(db.Model):
    
    __tablename_ = 'shelfs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    #book = db.relationship("BookModel", lazy='dynamic')

    #relacja z książką - czy backref dobrze napisane? nazwa tabeli czy klasa?
    def __init__(self, name, address, city_id):
        self.name = name
        self.address = address
        self.city_id = city_id

    def json(self):
        return {'name': self.name, 'address': self.address, 'books': [book.json() for book in self.book.all()]}

    @classmethod
    def find_by_name(cls, name):
        cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()
