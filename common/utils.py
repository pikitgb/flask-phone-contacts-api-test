import json
from bson.objectid import ObjectId

'''
This class JSONEncoder takes a JSON from MongoDB document and return the JSONObject
'''
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
