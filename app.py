import sys, os
from flask import *
from flask_restful import *
from resources.phones import PhoneController
from resources.phones import PhonesController


app = Flask(__name__)
api = Api(app)

# GET Phone/:Id
api.add_resource(PhoneController, '/phones/<phone_id>')

# GET/POST Phones
api.add_resource(PhonesController, '/phones')


if __name__ == '__main__':
    app.run(debug=True)
