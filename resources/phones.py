from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from flask_restful import *
from flask import *
from models.phone import PhoneDB
from common.utils import JSONEncoder

#----
parser = reqparse.RequestParser()
parser.add_argument('phone_id')
parser.add_argument('number', required=True)
parser.add_argument('id')

db = PhoneDB()
#----

# Simple controller for one Phone
class PhoneController(Resource):

    def get(self, phone_id):
        phone = db.find(phone_id)
        response = JSONEncoder().encode(phone)
        return response, 200

# Controller for multiple Phones
class PhonesController(Resource):

    # Get the list of phones
    def get(self):
        phones = db.all()
        response = []
        for phone in phones:
            response.append(JSONEncoder().encode(phone))
        return response, 200

    # Create a new phone
    def post(self):
        args = parser.parse_args()
        phone = {"number": args['number']}
        id = db.create(phone)
        if id != None:
            return JSONEncoder().encode({"status" : "ok", "message" : "Phone created successfully", "_id" : id }), 201
        else:
            return JSONEncoder().encode({"status": "error", "message": "Sorry. I can not create the phone now"}), 500
