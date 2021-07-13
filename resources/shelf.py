from flask_restful import Resource, reqparse
from models.shelf import ShelfModel

class Shelf(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('address', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('city_id', type=int, required=True, help="This field cannot be blank.")

    def get(self, name):
        shelf = ShelfModel.find_by_name(name)
        if shelf:
            return shelf.json()
        return {'message': 'Shelf not found'}, 404

    def post(self, name):
        if ShelfModel.find_by_name(name):
            return {'message': 'A shelf {} already exists.'.format(name)}, 400
        
        data = Shelf.parser.parse_args()
        shelf = ShelfModel(name, **data)
        try:
            shelf.save_to_db()
        except:
            return {'message': 'An error ocuured creating a shell'}, 500

#class ShellList chyba zbędna. bo mam wszystko w klasie wyżej - city 