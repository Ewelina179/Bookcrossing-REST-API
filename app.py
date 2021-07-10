from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_migrate import Migrate
from db import db


from security import authenticate, identity
from resources.user import UserRegister
from resources.city import City, CityList
from resources.shelf import Shelf

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "zmienic to. nie hardcoded ma być"

api = Api(app)

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()
    
jwt = JWT(app, authenticate, identity)



api.add_resource(CityList, '/cities')
api.add_resource(City, '/city/<string:name>')
api.add_resource(Shelf, '/shelf/<string:name>')
#api.add_resource(Book, '/book/<string:title>')
api.add_resource(UserRegister, '/register')
#nie jestem pewna co do endpointów

if __name__ == '__main__':
    app.run(port=5000, debug=True)