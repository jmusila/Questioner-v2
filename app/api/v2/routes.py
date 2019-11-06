"""
This file contains all the routes
"""

# Third party imports
from flask import Blueprint
from flask_restplus import Api

#Local imports
from .views.user import v2 as users_route
from .views.meetups import v2 as meetup_route
from .views.questions import v2 as quiz_route
from .views.comments import v2 as comments_route

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }}

version2 = Blueprint('version2', __name__, url_prefix="/api/v2")
api = Api(version2,     
    title ='Questioner',
    version='2.0',
    description='Questioner API with postgres',)
    
v2 = api.namespace(
    'v2', authorizations=authorizations)

api.add_namespace(users_route, path = "/auth")
api.add_namespace(meetup_route, path = "/meetups/upcoming")
api.add_namespace(quiz_route, path = "/meetups")
api.add_namespace(comments_route, path = "/questions")
