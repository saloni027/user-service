"""
    Module contains get_users function for getting a all user data from database
"""
from flask import request
from app.models import User
from app.utils import find_user_by_name, find_user_emails, find_user_phone_numbers


def get_users():
    """Get all Users with contact data

    Returns:
        _type_: Response list of all user_data objects or error message
    """
    response = []
    users = User.query.all()
    name = request.args.get("name")

    if name:
        users = find_user_by_name(name)
        if not users:
            response.append({"error_message": "User not found"})
            return response
        

    for user in users:

        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "emails": find_user_emails(user),
            "phone_numbers": find_user_phone_numbers(user),
        }
        response.append(user_data)

    return response
