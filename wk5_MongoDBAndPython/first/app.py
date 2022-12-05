import json
from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
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
        result = businesses.insert_one(new_business)
        new_business_id = result.inserted_id
        new_business_link = "http://localhost:5000/api/v1.0/businesses/" + str(new_business_id)
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
            {'_id': ObjectId(id)}, 
            {"$set": {
                    'name': request.form["name"], 
                    'town': request.form["town"], 
                    'rating': request.form["rating"]
                }}
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

# sub-document collection (reviews) by business id


@app.route("/api/v1.0/businesses/<string:id>/reviews", methods=["GET"])
def fetch_all_reviews(id):
    if len(id) == 24 and id.isalnum():
        business = businesses.find_one({'_id':ObjectId(id)})
        if business is not None:
            reviews = []
            for review in business['reviews']:
                review['_id'] = str(review['_id'])
                reviews.append(review)
            return make_response(jsonify(reviews), 200)
        else:
            return make_response(jsonify({'Error': 'Invalid business id'}), 404)
    else:
        return make_response(jsonify({'Error': 'Invalid business id'}), 404)

# create review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews", methods=['POST'])
def add_new_review(b_id):
    new_review = {
                '_id': ObjectId(),
                'username': request.form['username'],
                'comment': request.form['comment'],
                'stars': request.form['stars']
            }
    if  len(b_id) == 24 and b_id.isalnum():
        result = businesses.update_one(
            {'_id': ObjectId(b_id)}, 
            {'$push': {'reviews': new_review}}
        )

        if result.matched_count == 1:
            reviewlink = "http://localhost:5000/api/v1.0/businesses/" + b_id + "/review/" + str(new_review['_id'])
            return make_response(jsonify({'url': reviewlink}), 201)
        else:
            return make_response(jsonify({'Error': 'Invalid business id'}), 404)
    else:
        return make_response(jsonify({'Error': 'Invalid business id'}), 404)

# fetch one review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews/<string:r_id>", methods=['GET'])
def fetch_one_review(b_id, r_id):
    if len(b_id) == 24 and b_id.isalnum():
        if len(r_id) == 24 and r_id.isalnum():
            business = businesses.find_one(
                {'reviews._id':ObjectId(r_id)},
                {'reviews.$': 1})
            if business == None:
                return make_response(jsonify({'Error': 'Invalid review id'}), 404)
            if str(business['_id']) != b_id:
                return make_response(jsonify({'Error': 'Invalid business id'}), 404)
            business['reviews'][0]['_id'] = str(business['reviews'][0]['_id'])
            return make_response(jsonify(business['reviews'][0]), 200)
        else: 
            return make_response(jsonify({'Error': 'Invalid review id'}), 404)
    else:
        return make_response(jsonify({'Error': 'Invalid business id'}), 404)

# edit a review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews/<string:r_id>", methods=['PUT'])
def edit_one_review(b_id, r_id):        
    if len(b_id) == 24 and b_id.isalnum():
        if len(r_id) == 24 and r_id.isalnum():
            edited_review = {
                'reviews.$.username': request.form['username'], 
                'reviews.$.comment': request.form['comment'], 
                'reviews.$.stars': request.form['stars']
            }
            result = businesses.update_one(
                {
                    '_id': ObjectId(b_id), 
                    'reviews._id': ObjectId(r_id)}, 
                {
                    '$set': edited_review}
            )
            if result.matched_count == 1:
                edited_review_url = "http://127.0.0.1:5000/api/v1.0/businesses/" + b_id + "/reviews/" + r_id
                return make_response(jsonify({'url': edited_review_url}, 200))
            elif result.matched_count != 1 and businesses.find_one({'_id': ObjectId(b_id)}) is None:
                return make_response(jsonify({'Error': 'Invalid business id'}), 404)
            else:
                return make_response(jsonify({'Error': 'Invalid review id'}), 404)
        else: 
            return make_response(jsonify({'Error': 'Invalid review id'}), 404)
    else:
        return make_response(jsonify({'Error': 'Invalid business id'}), 404)

# delete a review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews/<string:r_id>", methods=['DELETE'])
def delete_one_review(b_id, r_id):
    if len(b_id) == 24 and b_id.isalnum():
        if len(r_id) == 24 and r_id.isalnum():
            result = businesses.update_one(
                {'_id': ObjectId(b_id)}, 
                {'$pull':{'reviews': {'_id': ObjectId(r_id)}}}
            )
            if result.matched_count == 1:
                return make_response(jsonify({}, 204))
            elif result.matched_count != 1 and businesses.find_one({'_id': ObjectId(b_id)}) is None:
                return make_response(jsonify({'Error': 'Invalid business id'}), 404)
            else:
                return make_response(jsonify({'Error': 'Invalid review id'}), 404)
        else: 
            return make_response(jsonify({'Error': 'Invalid review id'}), 404)
    else:
        return make_response(jsonify({'Error': 'Invalid business id'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
