import os
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource
from flask_restful import Api
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from application.flask_essentials import database

from application.resources.candidate import Candidate
from application.resources.election import Election
from application.resources.user import User
from application.resources.vote import Vote

def create_app():

    app = Flask( 'vote_api' )

    app.config.update( os.environ )

    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 400

    # the following line should probably be temporary
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app( app )
    api = Api( app )

    api.add_resource( Candidate, '/candidate/', '/candidate/<int:id>/' )
    api.add_resource( Election, '/election/', '/election/<int:id>/' )
    api.add_resource( User, '/user/', '/user/<int:id>/' )
    api.add_resource( Vote, '/vote/', '/vote/<int:id>/' )


    @app.errorhandler( ValidationError )
    def handle_invalid( error ):
        response = jsonify( error.messages )
        response.status_code = 422
        return response

    @app.errorhandler(  IntegrityError )
    def handle_integrity( error ):
        response = jsonify( {} )
        response.status_code = 422
        return response

    @app.errorhandler( NoResultFound )
    def handle_no_result( error ):
        response = jsonify( {} )
        response.status_code = 404
        return response

    return app

action_api = create_app()
