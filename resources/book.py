from flask_restful import Resource, reqparse
from models.book import BookModel
from models.shelf import ShelfModel

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('shelf_id', type=int, required=True, help="This field cannot be blank")
    parser.add_argument('is_on_shelf', type=bool, required=True, help="This cannot be blank")
    parser.add_argument('publishing_house', type=str, required=True, hel="This field cannot be blank")
    parser.add_argument('publication_date', type=str, required=False)

    def get(self, title):
        book = BookModel.find_by_title(title)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    def post(self, title):
        if BookModel.find_by_title(title):
            return {'message': 'Book {} already exist'.format(title)}, 400

        data = Book.parser.args()
        book = BookModel.find_by_title(title, **data)
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

    class BookList(Resource):
        def get(self, shelf_id):
            books=BookModel.query.filter_by(shelf_id=shelf_id).all()
            return {'book from shell {}.format(shell_id)': [x.json() for x in books]}
        #ten cały do poprawki. poczytaj o endpointach








