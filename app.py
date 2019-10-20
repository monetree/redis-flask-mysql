
from flask import Flask
from flask_restful import Api
from resources.store import StoreList, Store


app = Flask(__name__)
# mysql databse connection
# here flaskmy is the databse name and root, Thinonce is username and password for mysql databse respectively.

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Thinkonce@127.0.0.1:3306/flaskmy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

# this code is to create table in flaskmy database as per our schema if not exist
@app.before_first_request
def create_tables():
    db.create_all()

# api end points to create and retrive store

api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/create')

if __name__ == '__main__':
    from db import db
    # initializing databse to access it everywhere in our app
    db.init_app(app)
    app.run(port=5000, debug=True)