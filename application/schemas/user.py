"""Matching schema for User"""
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from application.flask_essentials import database
from application.models.User import UserModel


class UserSchema( ModelSchema ):
    """Matching marshmallow schema to User"""

    class Meta:
        """Meta object for User"""

        model = UserModel
        strict = True
        sqla_session = database.session
