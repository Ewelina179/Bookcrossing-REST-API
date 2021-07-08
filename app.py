from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
#import resources

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "zmienic to. nie hardcoded ma być"

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
    
jwt = JWT(app, authenticate, identity)



api.add_resource(Locations, '/locations')
api.add_resource(Location, '/location/<string:name>')
api.add_resource(BookShell, '/bookshell/<string:name>')
api.add_resource(Book, '/book/<string:title>')
api.add_resource(UserRegister, '/register')
#nie jestem pewna co do endpointów

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)