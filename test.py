import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# select database
db = client.bizDB
# select collection
businesses = db.biz

business = businesses.find_one(
            {
                '_id': ObjectId("63587573a7dadc591cf47699"), 
                'reviews._id': ObjectId("6358807135bdbc00a1842900")
            }, 
            {'reviews.$': 1})

print(business)