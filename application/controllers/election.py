from application.flask_essentials import database, marshmallow

from application.models.election import ElectionModel

def get_election_by_id( election_id ):
    return database.session.query( ElectionModel ).filter_by( id = election_id )

def create_election():
    pass

def update_election():
    pass

def delete_election():
    pass
