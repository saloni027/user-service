"""
    Contains User, Email and PhoneNumber Entities
"""
from app import db
from sqlalchemy.orm import validates


class User(db.Model):
    """
    The class representing the schema of the User table.
    :param id (Integer): Id of the user.
    :param first_name (String): First name of the user
    :param last_name (String): Last name of the user
    """

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    emails = db.relationship("Email", backref="user", lazy=True)
    phone_numbers = db.relationship("PhoneNumber", backref="user", lazy=True)

    def __str__(self):
        return "<User %s>" % self.first_name


class Email(db.Model):
    """
    The class representing the schema of the Email table.
    :param id (Integer): Id of the email.
    :param mail (String): Email id
    :param user_id (Integer): user_id associated with email instance
    """

    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(120), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    @validates("mail")
    def validate_email(self, key, email):
        assert "@" in email
        assert "." in email

        # if Email.query.filter(Email.mail == email).first():
        #     raise AssertionError('Email already exists')

        return email

    def __str__(self):
        return "<Email %s>" % self.mail


class PhoneNumber(db.Model):
    """
    The class representing the schema of the PhoneNumber table.
    :param id (Integer): Id of the PhoneNumber.
    :param number (String): Number
    :param user_id (Integer): user_id associated with phone_number instance
    """

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __str__(self):
        return "<PhoneNumber %s>" % self.id
