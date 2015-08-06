from datetime import datetime
from common.mongo import MongoConnect
from bson.objectid import ObjectId

# Data Access
class PhoneDB():
    def __init__(self):
        self.coll = MongoConnect().get_connection().phones

    def find(self, id):
        return self.coll.find_one({'_id': ObjectId(id)})

    def by_phone_number(self, number):
        return self.coll.find_one({'number': number})

    # Returns an array with the list of phones
    def all(self):
        return self.coll.find()

    def first(self):
        return self.coll.find()[0]

    def last(self):
        data = self.coll.find()
        return data[data.count - 1]

    def create(self, phone_hash):
        object = self.coll.insert_one(phone_hash)
        return object.inserted_id

