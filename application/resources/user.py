from application.schemas.user import UserSchema
from flask_restful import Resource

class User( Resource ):

    schema = UserSchema()

    def get( self ):
        pass

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
