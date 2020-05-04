from application.schemas.election import ElectionSchema
from flask_restful import Resource

class Election( Resource ):

    schema = ElectionSchema()

    def get( self, id ):
        pass

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
