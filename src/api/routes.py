"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    #We're on the receiving side so we have to make a request to receive from the user.

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    person = Person()
    #user = User()
    #user.email='darius@email.com'
    #user.password='newpass'
    #user.is_active=True
    print('Hello from /hello. Here is your user:')
    #print(user.serialize)
    all_people = Person.query.all()
    all_people = list(map(lambda x: x.serialize(), all_people))
    #db.session.add(user)

    #translate code to sql and save
    #db.session.commit()

    return jsonify(response_body), 200
