from flask_restful import Resource

from application.schemas.vote import VoteSchema
from application.controllers.vote import get_vote_by_id

class Vote( Resource ):

    schema = VoteSchema()

    def get( self, id ):
        return self.schema.dump(
            get_vote_by_id( vote_id = id )
        ), 200

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
