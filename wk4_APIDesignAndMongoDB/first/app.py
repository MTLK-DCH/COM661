from flask import Flask, jsonify, make_response, request
import uuid
import MyUtils.utils

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


businesses = {}

# index print hello world


@app.route("/", methods=["GET"])
def index():
    return make_response("<h1>Hello world</h1>", 200)

# get all of the businesses


@app.route("/api/v1.0/businesses", methods=["GET"])
def show_all_businesses():
    return make_response(jsonify(businesses), 200)

# get one business by id


@app.route("/api/v1.0/businesses/<string:id>", methods=["GET"])
def show_one_business(id):
    return make_response(jsonify(businesses[id]), 200)

# create a new business


@app.route("/api/v1.0/businesses", methods=["POST"])
def add_business():
    next_id = uuid.uuid1()
    new_business = {
        "id": next_id,
        "name": request.form["name"],
        "town": request.form["town"],
        "rating": request.form["rating"],
        "reviews": []
    }
    print(new_business)
    businesses.append(new_business)
    return make_response(jsonify(new_business), 201)

# edit the business by id


@app.route("/api/v1.0/businesses/<string:id>", methods=["PUT"])
def edit_business(id):
    print(request.form)
    business = businesses[id]
    print('editting')
    business["name"] = request.form["name"]
    business["town"] = request.form["town"]
    business["rating"] = request.form["rating"]
    return make_response(jsonify(business), 200)

# delete a business by id


@app.route("/api/v1.0/businesses/<string:id>", methods=["DELETE"])
def delete_business(id):
    businesses.pop(id)
    return make_response(jsonify({}), 200)

# sub-document collection (reviews) by id


@app.route("/api/v1.0/businesses/<string:id>/reviews", methods=["GET"])
def fetch_all_reviews(id):
    return make_response(jsonify(businesses[id]['reviews']), 200)

# create review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews", methods=['POST'])
def add_new_review(b_id):
    for business in businesses:
        if business['id'] == b_id:
            if len(business['reviews']) == 0:
                new_review_id = 1
            else:
                new_review = business['reviews'][-1]['id'] + 1
            new_review = {
                'id': new_review_id,
                'username': request.form['username'],
                'comment': request.form['comment'],
                'stars': request.form['stars']
            }
            business['reviews'].append(new_review)
            break
    return make_response(jsonify(new_review), 201)

# fetch one review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews/<int:r_id>", methods=['GET'])
def fetch_one_review(b_id, r_id):
    for business in businesses:
        if business['id'] == b_id:
            for review in business['reviews']:
                if review['id'] == r_id:
                    return make_response(jsonify(review), 200)
            return make_response('review id error', 404)
        else:
            return make_response('business id error', 404)

# edit a review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews/<int:r_id>", methods=['PUT'])
def edit_one_review(b_id, r_id):
    for business in businesses:
        if business['id'] == b_id:
            for review in business['reviews']:
                if review['id'] == r_id:
                    review['comment'] = request.form['new_comment']
                    return make_response(jsonify(review), 200)
            return make_response('review id error', 404)
        else:
            return make_response('business id error', 404)

# delete a review


@app.route("/api/v1.0/businesses/<string:b_id>/reviews/<int:r_id>", methods=['DELETE'])
def delete_one_review(b_id, r_id):
    for business in businesses:
        if business['id'] == b_id:
            for review in business['reviews']:
                if review['id'] == r_id:
                    business['reviews'].remove(review)
                    return make_response({}, 200)
            return make_response('review id error', 404)
        else:
            return make_response('business id error', 404)


if __name__ == "__main__":
    businesses = MyUtils.utils.generate_dummy_daty(100)
    app.run(debug=True)
