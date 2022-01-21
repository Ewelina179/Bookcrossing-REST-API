from flask_restful import Resource, reqparse
from models.book import BookModel
from models.shelf import ShelfModel
from datetime import datetime

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('shelf_id', type=int, required=True, help="This field cannot be blank")
    parser.add_argument('is_on_shelf', type=bool, required=True, help="This cannot be blank")
    parser.add_argument('publishing_house', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('publication_date', type=str, required=False)

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
        shelf_id = data["shelf_id"]
        is_on_shelf = data['is_on_shelf']
        publishing_house = data['publishing_house']
        publication_date = data['publication_date']
        shelf = ShelfModel.query.filter_by(id=shelf_id).first()
        
        expiration_year  = int(publication_date[:4])
        expiration_month = int(publication_date[5:7])
        expiration_date = int(publication_date[8:10])
        expiration_date = datetime(expiration_year,expiration_month,expiration_date)

        book = BookModel(author=author, title=title, shelf_id=shelf.id, is_on_shelf=is_on_shelf, publishing_house=publishing_house, publication_date=expiration_date)
        
        try:
            book.save_to_db()
            print("hejo")
        except:
            return {'message': 'An error occurred creating a book'}, 500
        return book.json(), 201

    def delete(self, title):
        book = BookModel.find_by_title(title)
        if book:
            book.delete_from_db()
        return {'message': 'Book deleted'}

class BookShelfList(Resource):
    def get(self, name):
        shelf_id = ShelfModel.query.filter_by(name=name).first()
        books=BookModel.query.filter_by(shelf_id=shelf_id.id).all()
        return {'book from shelf': [x.json() for x in books]}

class BookList(Resource):
    def get(self):
        books = BookModel.query.all()
        return {'books': [x.json() for x in books]}









