from pymongo import MongoClient
import random

client = MongoClient("mongodb://127.0.0.1:27017")
# select database
db = client.bizDB
# select collection
businesses = db.biz

for business in businesses:
    businesses.update_one(
        {
            'id': business['_id']
        }, 
        {
            '$set':{
                'num_emploees': random.randint(1, 100), 
                'profit': []
            }
        }
    )