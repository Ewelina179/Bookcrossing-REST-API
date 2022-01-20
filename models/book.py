from datetime import date
import json
from db import db

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(64))
    title = db.Column(db.String(128))
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelfs.id'))
    is_on_shelf = db.Column(db.Boolean)
    publishing_house = db.Column(db.String(128))
    publication_date = db.Column(db.Date)
    shelf = db.relationship('ShelfModel')

    def __init__(self, author, title, shelf_id, is_on_shelf, publishing_house, publication_date):
        self.author = author
        self.title = title
        self.shelf_id = shelf_id
        self.is_on_shelf = is_on_shelf
        self.publishing_house = publishing_house
        self.publication_date = publication_date

    def json(self):
        print({'title': self.title, 'author': self.author, 'shelf': self.shelf_id, 'is available': self.is_on_shelf, 'publishing house': self.publishing_house, 'publication date': self.publication_date})
        return {'title': self.title, 'author': self.author, 'shelf': self.shelf_id, 'is available': self.is_on_shelf, 'publishing house': self.publishing_house, 'publication date': json.dumps(self.publication_date, cls=ComplexEncoder)}

    @classmethod
    def find_by_title(cls, title):
        print(title)
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


