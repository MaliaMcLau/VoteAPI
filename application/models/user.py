from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import MEDIUMINT
from flask import current_app

from application.flask_essentials import database

class UserModel( database.Model ):
    """Details the SQL schema for user"""

    __tablename__ = 'user'
    id = database.Column(
        SMALLINT, primary_key = True, autoincrement = True, nullable = False
    )
    name = database.Column(
        database.String(20), nullable = False
    )
    username_hash = database.Column(
        database.String(50), nullable = False
    )
    password_hash = database.Column(
        database.String(100), nullable = False
    )
