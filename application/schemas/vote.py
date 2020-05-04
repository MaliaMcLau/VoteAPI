"""Matching schema for Vote"""
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from application.flask_essentials import database
from application.models.vote import VoteModel


class VoteSchema( ModelSchema ):
    """Matching marshmallow schema to Vote"""

    class Meta:
        """Meta object for Vote"""

        model = VoteModel
        strict = True
        sqla_session = database.session
