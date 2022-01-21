from flask_restful import Resource, reqparse
from models.book import BookModel
from models.shelf import ShelfModel
from datetime import datetime

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('shelf_name', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('is_on_shelf', type=bool, required=True, help="This cannot be blank")
    parser.add_argument('publishing_house', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('publication_year', type=str, required=False)

    def get(self, title):
        print(title)
        book = BookModel.find_by_title(title)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    def post(self, title):
        if BookModel.find_by_title(title):
            return {'message': 'Book {} already exist'.format(title)}, 400
        data = Book.parser.parse_args()
        author = data["author"]
        shelf_name = data["shelf_name"]
        is_on_shelf = data['is_on_shelf']
        publishing_house = data['publishing_house']
        publication_year = data['publication_year']
        print(publication_year)

        shelf = ShelfModel.query.filter_by(name=shelf_name).first()

        if not shelf:
            return {'message': 'Shelf {} not exist.'.format(shelf_name)}, 400

        book = BookModel(author=author, title=title, shelf_id=shelf.id, is_on_shelf=is_on_shelf, publishing_house=publishing_house, publication_year=publication_year)

        try:
            book.save_to_db()
        except:
            return {'message': 'An error occurred creating a book'}, 500
        return book.json(), 201

    def delete(self, title):
        book = BookModel.find_by_title(title)
        if book:
            book.delete_from_db()
            return {'message': 'Book deleted'}
        else:
            return {'message': 'Book not in db'}


class BookShelfList(Resource):
    def get(self, name):
        shelf_id = ShelfModel.query.filter_by(name=name).first()
        books=BookModel.query.filter_by(shelf_id=shelf_id.id).all()
        return {'book from shelf': [x.json() for x in books]}

class BookList(Resource):
    def get(self):
        books = BookModel.query.all()
        return {'books': [x.json() for x in books]}









