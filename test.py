import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# select database
db = client.bizDB
# select collection
businesses = db.biz

business = businesses.find(
            {'reviews.username': 'a'}, 
            {'reviews.$': 1})

print(business)