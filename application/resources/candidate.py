from application.schemas.candidate import CandidateSchema
from flask_restful import Resource

class Candidate( Resource ):

    schema = CandidateSchema()

    def get( self, id ):
        pass

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
