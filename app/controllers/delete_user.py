"""
    Module contains delete_user function for deleting user data from database
"""

from app.utils import find_user_by_id, delete_obj


def delete_user(id):
    """Deletes a user with the given id

    Args:
        id (int): id of the user

    Returns:
        list: list containing success or error response
    """

    response = []

    user = find_user_by_id(id)
    if not user:
        response.append({"error_message": "User not found"})
        return response

    delete_obj(user)
    success_response = {"message": "User deleted Successfully"}
    response.append(success_response)
    return response
