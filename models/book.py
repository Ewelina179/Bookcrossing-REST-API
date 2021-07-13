from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(64))
    title = db.Column(db.String(128))
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelfs.id'))
    is_on_shelf = db.Column(db.Boolean)
    publishing_house = db.Column(db.String(128))
    publication_date = db.Column(db.DateTime)
    shelf = db.relationship('ShelfModel')

    def __init__(self, author, title, shelf_id, is_on_shelf, publishing_house, publication_date):
        self.author = author
        self.title = title
        self.shelf_id = shelf_id
        self.is_on_shell = is_on_shelf
        self.publishing_house = publishing_house
        self.publication_date = publication_date

    def json(self):
        return {'title': self.title, 'author': self.author, 'shelf': self.shelf_id, 'is available': self.is_on_shelf, 'publishing house': self.publishing_house, 'publication date': self.publishing_date}

    @classmethod
    def find_by_title(cls, title):
        cls.find_by_title(title=title).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


