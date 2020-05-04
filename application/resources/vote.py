from application.schemas.vote import VoteSchema
from flask_restful import Resource

class Vote( Resource ):

    schema = VoteSchema()

    def get( self, id ):
        pass

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
