from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from nusa_jwt_auth import NUSAJwtManager

database = SQLAlchemy()
marshmallow = Marshmallow()
