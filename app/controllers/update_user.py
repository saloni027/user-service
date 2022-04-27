"""
    Module contains update_user function for updating a single user data to database
"""
from app.utils import (
    find_user_by_id,
    find_email_by_id,
    find_email_by_mail,
    find_email_by_mail,
    find_phone_no_by_id,
    find_phone_no_by_number,
    create_phone_no,
    create_email,
    find_user_emails,
    find_user_phone_numbers,
    delete_obj,
    commit_obj,
)


def update_user(request_data, id):
    """Updates the data for the user

    Args:
        request_data (json dict): json dict object containing user data to update

    Returns:
        list: list of dict object as Response or error message
    """
    response = []
    user = find_user_by_id(id)
    if not user:
        response.append({"error_message": "User not found"})
        return response

    user.first_name = request_data["first_name"]
    user.last_name = request_data["last_name"]
    emails = request_data["emails"]
    phone_numbers = request_data["phone_numbers"]

    for email in emails:

        if "id" in email:  # update existing email

            email_obj = find_email_by_id(email["id"])

            if "is_delete" in email:

                delete_obj(email_obj)

            else:

                email_obj.mail = email["mail"]
                commit_obj()

        else:  # Create new email
            email_obj = find_email_by_mail(email["mail"])
            if not email_obj:
                try:

                    email_obj = create_email(email["mail"], user.id)

                except AssertionError as ex:

                    response.append({"error_message": "Email Validation Failed"})

                    return response

    for phone_number in phone_numbers:

        if "id" in phone_number:  # update existing phone_number

            phone_obj = find_phone_no_by_id(phone_number["id"])

            if "is_delete" in phone_number:

                delete_obj(phone_obj)

            else:

                phone_obj.number = phone_number["number"]
                commit_obj()
        else:
            phone_no_obj = find_phone_no_by_number(phone_number["number"])

            if not phone_no_obj:
                phone_no_obj = create_phone_no(phone_number["number"], user.id)

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
