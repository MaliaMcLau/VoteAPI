from application.flask_essentials import database, marshmallow

from application.models.candidate import CandidateModel

def get_candidate_by_id( candidate_id ):
    return database.session.query( CandidateModel ).filter_by( id = candidate_id )

def get_candidates_by_election( election_id ):
    return database.session.query( CandidateModel ).filter_by( id = election_id )

def create_candidate():
    pass

def update_candidate( candidate_id ):
    pass

def delete_candidate( candidate_id ):
    pass
