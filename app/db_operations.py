"""
    Module containing database operations
"""
from app import db


def save_to_db(obj):
    """saves an object to the database

    Args:
        obj (obj): module instance
    """

    db.session.add(obj)
    commit_to_db()


def commit_to_db():
    """Commits an object to the database

    Args:
        obj (obj): module instance
    """

    db.session.commit()


def delete_from_db(obj):
    """Deletes an object from the database

    Args:
        obj (obj): module instance
    """

    db.session.delete(obj)
    db.session.commit()
