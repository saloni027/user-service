"""
    Utilities for processing all API requests
"""
from app.models import User, Email, PhoneNumber
from app.db_operations import save_to_db, commit_to_db, delete_from_db


def find_user_by_id(id):
    """Finds user by given id

    Args:
        id (int): _description_

    Returns:
        app.models.User: Return user model instance with the given id
    """
    user = User.query.filter_by(id=id).first()
    return user


def find_user_by_name(name):

    """Finds user by name

    Args:
        name (str): firstname of the user

    Returns:
        list: list of user objects with the given name
    """

    users_by_name = User.query.filter_by(first_name=name).all()
    return users_by_name


def find_user_emails(user_obj):
    """Finds all emails attached to the given user object

    Args:
        user_obj (app.models.User): user model instance

    Returns:
        list: list of emails attached to the given user object
    """

    emails = []

    for email in user_obj.emails:

        email_data = {"id": email.id, "mail": email.mail}
        emails.append(email_data)

    return emails


def find_user_phone_numbers(user_obj):
    """Finds all phone_numbers attached to the given user object

    Args:
        user_obj (app.models.User): user model instance

    Returns:
        list: list of phone_numbers attached to the given user object
    """

    phone_numbers = []

    for phone_number in user_obj.phone_numbers:

        phone_data = {"id": phone_number.id, "number": phone_number.number}
        phone_numbers.append(phone_data)

    return phone_numbers


def find_email_by_id(email_id):
    email = Email.query.filter_by(id=email_id).first()
    return email


def find_phone_no_by_id(id):
    phone_no = PhoneNumber.query.filter_by(id=id).first()
    return phone_no


def find_email_by_mail(mail):

    email_obj = Email.query.filter_by(mail=mail).first()
    return email_obj


def find_phone_no_by_number(phone_number):

    phone_no_obj = PhoneNumber.query.filter_by(number=phone_number).first()
    return phone_no_obj


def create_user(request_data):

    user = User(
        first_name=request_data["first_name"], last_name=request_data["last_name"]
    )
    save_to_db(user)
    return user


def create_email(email, user_id):

    email_obj = Email(mail=email, user_id=user_id)
    save_to_db(email_obj)
    return email_obj


def create_phone_no(phone_number, user_id):

    phone_no_obj = PhoneNumber(number=phone_number, user_id=user_id)
    save_to_db(phone_no_obj)
    return phone_no_obj


def delete_obj(obj):

    delete_from_db(obj)


def commit_obj():

    commit_to_db()
