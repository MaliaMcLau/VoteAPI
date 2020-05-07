from application.flask_essentials import database, marshmallow

from application.models.candidate import CandidateModel

def get_candidate_by_id( id ):
    return database.session.query( CandidateModel ).filter_by( id = id )

def create_candidate():
    pass

def update_candidate( candidate_id ):
    pass

def delete_candidate( candidate_id ):
    pass
