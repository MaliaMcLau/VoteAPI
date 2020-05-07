from flask_restful import Resource

from application.schemas.election import ElectionSchema
from application.resources import get_election_by_id

class Election( Resource ):

    schema = ElectionSchema()

    def get( self, id ):
        return self.schema.dump(
            get_election_by_id( election_id = id )
        ), 200

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
