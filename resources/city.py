from flask_restful import Resource, reqparse
from models.city import CityModel

class City(Resource):
    def get(self, name):
        city = CityModel.find_by_name(name)
        if city:
            return city.json()
        return {'message': 'City not found'}, 404

    def post(self, name):
        if CityModel.find_by_name(name):
            return {'message': "A city with name {} already exists.".format(name)}, 400

        city = CityModel(name)
        try:
            city.save_to_db()
        except:
            return {"message": "An error occured creating the store"}, 500

class CityList(Resource):
    def get(self):
        cities = CityModel.query.all()
        return {'cities': [x.json() for x in cities]}
