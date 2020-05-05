from application.flask_essentials import database, marshmallow

from application.models.user import UserModel

def get_user_by_id( user_id ):
    return database.session.query( UserModel ).filter_by( id = user_id )

def create_user():
    pass

def update_user():
    pass

def delete_user():
    pass
