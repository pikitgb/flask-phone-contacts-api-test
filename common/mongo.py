import sys
from pymongo import MongoClient
from pymongo.errors import *

class MongoConnect:
    def get_connection(self):
        client = MongoClient('mongodb://localhost:27017')
        db = client.test_phone_database
        return db

