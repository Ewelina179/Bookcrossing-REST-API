from flask_restful import Resource, reqparse
from models.book import BookModel

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('shelf_id', type=int, requied=True, help="This field cannot be blank")
    parser.add_argument('is_on_shelf', type=bool, required=True, help="This cannot be blank")
    parser.add_argument('publishing_house', type=str, required=True, hel="This field cannot be blank")
    parser.add_argument('publication_date', type=str, required=False)



