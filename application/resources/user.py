from flask_restful import Resource

from application.schemas.user import UserSchema
from application.controllers.user import get_user_by_id

class User( Resource ):

    schema = UserSchema()

    def get( self, id ):
        return self.schema.dump(
            get_user_by_id( user_id = id )
        ), 200

    def post( self ):
        pass

    def put( self ):
        pass

    def delete( self ):
        pass
