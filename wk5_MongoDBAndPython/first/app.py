from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")
# select database
db = client.bizDB
# select collection
businesses = db.biz

# index print hello world


@app.route("/", methods=["GET"])
def index():
    return make_response("<h1>Hello world</h1>", 200)

# get all of the businesses


@app.route("/api/v1.0/businesses", methods=["GET"])
def show_all_businesses():
    page_num, page_size = 1, 10
    if request.arg.get('pn'):
        page_num = int(request.arg.get('pn'))
    if request.arg.get('ps'):
        page_size = int(request.arg.get('ps'))
    page_start = (page_size * (page_num -1))

    data2return = []
    for business in businesses.find().skip(page_start).limit(page_size):
        business['_id'] = str(business['_id'])
        for review in business['reviews']:
            review['_id'] = str(review['_id'])
        data2return.append(business)

    return make_response(jsonify(data2return), 200)

# get one business by id


@app.route("/api/v1.0/businesses/<string:id>", methods=["GET"])
def show_one_business(id):
    if len(id) == 24 and id.isalnum():
        business = businesses.find_one({'_id':ObjectId(id)})
        if business is not None:
            business['_id'] = str(business['_id'])
            for review in business['reviews']:
                review['_id'] = str(review['_id'])
            return make_response(jsonify(business), 200)
        else:
            return make_response({'Error': 'Invalid business id'}, 404)
    else:
        return make_response({'Error': 'Invalid business id'}, 404)

# create a new business


@app.route("/api/v1.0/businesses", methods=["POST"])
def add_business():
    if 'name' in request.form \
        and 'town' in request.form \
        and 'rating' in request.form:
        new_business = {
            "name": request.form["name"],
            "town": request.form["town"],
            "rating": request.form["rating"],
            "reviews": []
        }
        new_business_id = businesses.insert_one(new_business)
        new_business_link = "http://localhost:5000/api/v1.0/businesses/" + str(new_business_id.inserted_id)
        return make_response(jsonify(new_business_link), 201)
    else:
        return make_response(jsonify({"Error": "Missing form data"}), 404)

# edit the business by id


@app.route("/api/v1.0/businesses/<string:id>", methods=["PUT"])
def edit_business(id):
    if 'name' in request.form \
        and 'town' in request.form \
        and 'rating' in request.form:
        result = businesses.update_one(
            {
                '_id': ObjectId(id)
            }, 
            {
                "$set": {
                    'name': request.form["name"], 
                    'town': request.form["town"], 
                    'rating': request.form["rating"]
                }
            }
        )
        if result.matched_count == 1:
            edied_business_link = "http://localhost:5000/api/v1.0/businesses/" + id
            return make_response(jsonify({'url': edied_business_link}), 200)
        else:
            return make_response(jsonify({"Error": "Invalide business id"}), 404)
    else:
        return make_response(jsonify({"Error": "Missing form data"}), 404)

# delete a business by id


@app.route("/api/v1.0/businesses/<string:id>", methods=["DELETE"])
def delete_business(id):
    result = businesses.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return make_response(jsonify({}), 204)
    else:
        return make_response(jsonify({'Error': 'Invalid business id'}))

if __name__ == "__main__":
    app.run(debug=True)
