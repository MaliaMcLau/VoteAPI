from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import MEDIUMINT
from flask import current_app

from application.flask_essentials import database

class CandidateModel( database.Model ):
    """Details the SQL schema for candidate"""

    __tablename__ = 'candidate'
    id = database.Column(
        SMALLINT, primary_key = True, autoincrement = True, nullable = False
    )
    name = database.Column(
        database.String(200), nullable = False
    )
    election_id = database.Column(
        SMALLINT, nullable = False
    )
