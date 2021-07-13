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

    #dodać metody konieczne
