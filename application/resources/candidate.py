from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from application.schemas.candidate import CandidateSchema
from application.controllers.candidate import get_candidate_by_id

class Candidate( Resource ):

    schema = CandidateSchema()

    def get( self, candidate_id = None, election_id = None ):

        if ( candidate_id == None and election_id == None ):
            raise IntegrityError

        id = candidate_id if ( candidate_id != None ) else election_id

        return self.schema.dump(
            get_candidate_by_id( id )
        ), 200

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
