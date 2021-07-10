from flask_restful import Resource
from models.shelf import ShelfModel

class Shelf(Resource):
    def get(self, name):
        pass

    def post(self, name):
        pass

#class ShellList chyba zbędna. bo mam wszystko w klasie wyżej - city 