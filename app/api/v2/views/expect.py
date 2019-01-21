
#Third party imports 
from flask_restplus import fields, Namespace 

class UserRegister:
    """
    User signup input data

    """
    v2 = Namespace('Users', description = 'User Routes')
    users = v2.model('User', {
        'firstname': fields.String(required=True, description='This is the user firstname'),
        'lastname': fields.String(required=True, description='This is the user lastname'),
        'email': fields.String(required=True, description='The user email'),
        'phoneNumber': fields.String(required=True, description='This phone number of the user'),
        'username': fields.String(required=True, description='This is the username'),
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
        'title': fields.String(required=True, description='The meetup topic'),
        'happeningOn': fields.String(required=True, description='The time the meetup will happen'),
        'tags': fields.String(required=True, description='The meetup tags'),
    })
    