"""Matching schema for Candidate"""
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from application.flask_essentials import database
from application.models.candidate import CandidateModel


class CandidateSchema( ModelSchema ):
    """Matching marshmallow schema to Candidate"""

    class Meta:
        """Meta object for Candidate"""

        model = CandidateModel
        strict = True
        sqla_session = database.session
