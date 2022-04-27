"""
    Module contains add_user function for adding user data to database
"""
from app.utils import (
    create_user,
    find_email_by_mail,
    create_email,
    find_phone_no_by_number,
    create_phone_no,
)


def add_user(request_data):
    """Adds user data to the database and returns response

    Args:
        request_data (json dict): dict containig user data given as payload in the post request.

    Returns:
        list: Returns list of dict objects as Response or error_message
    """
    response = []
    request_emails = request_data.get("emails", None)
    request_phone_numbers = request_data.get("phone_numbers", None)
    user = create_user(request_data)

    created_emails = []
    created_phone_numbers = []

    if request_emails:

        for email in request_data["emails"]:

            email_obj = find_email_by_mail(email["mail"])
            if not email_obj:
                try:
                    email_obj = create_email(email["mail"], user.id)

                except AssertionError as ex:

                    response.append({"error_message": "Email Validation Failed"})
                    return response

                email_data = {"id": email_obj.id, "mail": email_obj.mail}
                created_emails.append(email_data)

    if request_phone_numbers:

        for phone_number in request_data["phone_numbers"]:

            phone_obj = find_phone_no_by_number(phone_number["number"])
            if not phone_obj:
                phone_obj = create_phone_no(phone_number["number"], user.id)
                phone_number_data = {"id": phone_obj.id, "number": phone_obj.number}
                created_phone_numbers.append(phone_number_data)

    user_data = {
        "id": user.id,
        "first_name": request_data["first_name"],
        "last_name": request_data["last_name"],
        "emails": created_emails,
        "phone_numbers": created_phone_numbers,
    }
    response.append(user_data)
    return response
