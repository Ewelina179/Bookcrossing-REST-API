from flask import Flask, jsonify
from flask_restful import Resource, Api
from security import authenticate, identity

app = Flask(__name__)

app.secret_key = "zmienic to. nie hardcoded ma być"

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Locations, '/locations')
api.add_resource(Location, '/location/<string:name>')
api.add_resource(BookShell, '/bookshell/<string:name>')
api.add_resource(Book, '/book/<string:title>')
api.add_resource(UserRegister, '/register')
#nie jestem pewna co do endpointów

app.run()