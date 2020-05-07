from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from application.schemas.candidate import CandidateSchema
from application.controllers import get_candidate_by_id, get_candidates_by_election

class Candidate( Resource ):

    schema = CandidateSchema()

    def get( self, candidate_id = None, election_id = None ):

        if ( candidate_id == None and election_id == None ):
            raise IntegrityError

        return self.schema.dump(
            get_candidate_by_id( candidate_id = candidate_id, election_id = election_id )
        ), 200

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
