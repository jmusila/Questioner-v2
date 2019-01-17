"""
This file contains all the routes
"""

# Third party imports
from flask import Blueprint
from flask_restplus import Api

#Local imports
from .views.user import v2 as users_route
from .views.meetups import v2 as meetup_route

    
version2 = Blueprint('version2', __name__, url_prefix="/api/v2")
api = Api(version2,     
    title ='Questioner',
    version='2.0',
    description='Questioner API with postgres',)
    
v2 = api.namespace(
    'v2')

api.add_namespace(users_route, path = "/auth")
api.add_namespace(meetup_route, path = "/meetups/upcoming")

