from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import MEDIUMINT
from flask import current_app

from application.flask_essentials import database

class ElectionModel( database.Model ):
    """Details the SQL schema for election"""

    __tablename__ = 'election'
    id = database.Column(
        SMALLINT, primary_key = True, autoincrement = True, nullable = False
    )
    name = database.Column(
        database.String(20), nullable = False
    )
    start_date_utc = database.Column(
        database.DateTime, nullable = False
    )
    duration = database.Column(
        database.MEDIUMINT, nullable = False
    )
    type = database.Column(
        database.String(10), nullable = False
    )
