from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import MEDIUMINT
from flask import current_app

from application.flask_essentials import database

class VoteModel( database.Model ):
    """Details the SQL schema for vote"""

    __tablename__ = 'vote'
    id = database.Column(
        SMALLINT, primary_key = True, autoincrement = True, nullable = False
    )
    user_id = database.Column(
        SMALLINT, nullable = False
    )
    election_id = database.Column(
        SMALLINT, nullable = False
    )
    candidate_id = database.Column(
        SMALLINT, nullable = False
    )
    cast_date_utc = database.Column(
        database.DateTime, nullable=True
    )
