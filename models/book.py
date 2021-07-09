from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(64))
    title = db.Column(db.String(128))
    shell_id = db.Column(db.Integer, db.ForeignKey('shells.id'))
    is_on_shell = (db.Bolean)
    publishing_house = db.Column(db.String(128))
    publication_date = db.Column(db.DateTime)

    #dodać metody konieczne
