"""
    Module contains get_user function for getting a single user data from database
"""
from app.utils import find_user_by_id, find_user_emails, find_user_phone_numbers


def get_user(id):
    """Gets a single user data

    Args:
        id (int): _description_

    Returns:
        list: list of dict objects with user data or error message
    """
    response = []
    user = find_user_by_id(id)
    if not user:
        response.append({"error_message": "User not found"})
        return response

    emails = find_user_emails(user)
    phone_numbers = find_user_phone_numbers(user)

    user_data = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "emails": emails,
        "phone_numbers": phone_numbers,
    }
    response.append(user_data)
    return response
