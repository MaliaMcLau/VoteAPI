"""Matching schema for Election"""
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from application.flask_essentials import database
from application.models.election import ElectionModel


class ElectionSchema( ModelSchema ):
    """Matching marshmallow schema to Election"""

    class Meta:
        """Meta object for Election"""

        model = ElectionModel
        strict = True
        sqla_session = database.session
