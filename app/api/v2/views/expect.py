
#Third party imports 
from flask_restplus import fields, Namespace 

class UserRegister:
    """
    User signup input data

    """
    v2 = Namespace('Users', description = 'User Routes')
    users = v2.model('User', {
        'fname': fields.String(required=True, description='This is the user firstname'),
        'lname': fields.String(required=True, description='This is the user lastname'),
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(required=True, description='The user password'),
    })
class UserLogin:
    """
    User login input data 
    """
    v2 = Namespace('Users', description='Users Routes')
    login = v2.model('User', {
        'email': fields.String(required=True, description='The user email address'),
        'password': fields.String(required=True, description='The user password')
    })

class MeetupModel:
    """
    Meetups input data

    """
    v2 = Namespace('Meetups', description = 'Meetups Routes')
    meetups = v2.model('Meetup', {
        'location': fields.String(required=True, description='This is the place of the meetup'),
        'images': fields.String(required=True, description='This is the image of the meetup'),
        'topic': fields.String(required=True, description='The meetup topic'),
        'happeningOn': fields.String(required=True, description='The time the meetup will happen'),
        'tags': fields.String(required=True, description='The meetup tags'),
    })