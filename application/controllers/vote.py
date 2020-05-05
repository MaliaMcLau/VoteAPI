from application.flask_essentials import database, marshmallow

from application.models.vote import VoteModel

def get_vote_by_id( vote_id ):
    return database.session.query( VoteModel ).filter_by( id = vote_id )

def get_vote_by_user_id( user_id ):
    return database.session.query( VoteModel ).filter_by( id = user_id )

def create_vote( vote_id ):
    pass

def update_vote( vote_id ):
    pass

def delete_vote( vote_id ):
    pass
