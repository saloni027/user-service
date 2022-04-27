"""
    Contains all view functions for GET, POST, PUT and DELETE requests
"""
from flask import jsonify, request, make_response
from app import app, db
from app.models import User, Email, PhoneNumber
from app.controllers import get_users, get_user, add_user, update_user, delete_user


@app.route("/")
def index():
    """Index View

    Returns:
        _type_: Returns string response
    """
    return "API started!!"


@app.route("/users")
def get_users_view():
    """View function for getting all users data

    Returns:
        _type_: Response list along with the status code
    """

    response = get_users.get_users()
    
    if response:
    
        if "error_message" in response[0]:
            return make_response(jsonify(response), 404)

    return make_response(jsonify(response), 200)


@app.route("/users/<int:id>")
def get_user_view(id):
    """View function for getting single user data

    Args:
        id (int): id of the user

    Returns:
        list of dict: Response as a list of dictionary
    """
    response = get_user.get_user(id)

    if "error_message" in response[0]:
        return make_response(jsonify(response), 404)

    return make_response(jsonify(response), 200)


@app.route("/users", methods=["POST"])
def add_users_view():
    """Add a new user data

    Returns:
        list: list of dict objects containg user data which got added to db
    """
    request_data = request.get_json()

    response = add_user.add_user(request_data)
    if "error_message" in response[0]:
        return make_response(jsonify(response), 404)

    return make_response(jsonify(response), 201)


@app.route("/users/<int:id>", methods=["PUT"])
def update_user_view(id):
    """View functiona for Updating user data

    Args:
        id (int): id of the user

    Returns:
        list: list of json dict of updated user data
    """
    request_data = request.get_json()
    response = update_user.update_user(request_data, id)
    if "error_message" in response[0]:
        return make_response(jsonify(response), 404)

    return make_response(jsonify(response), 200)


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user_view(id):
    """View function for deleting user

    Args:
        id (int): id of the user

    Returns:
        list: list of json dict containig response message
    """
    response = delete_user.delete_user(id)
    if "error_message" in response[0]:
        return make_response(jsonify(response), 404)

    return make_response(jsonify(response), 200)
