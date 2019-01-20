#Third party imports
from flask_restplus import Resource
from flask import request, abort
from werkzeug.security import check_password_hash 
from .helpers import get_user_by_email, get_user_by_username
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.v2.models.user import User
from app.api.v2.views.expect import UserRegister
from app.api.common.validators import valid_email, new_user_validator

new_user = UserRegister().users
v2 = UserRegister().v2

@v2.route('/signup')
class SignUp(Resource):

    @v2.expect(new_user, validate = True)
    def post(self):
        '''Sign up a user'''
        data = request.get_json()
        if not new_user_validator(data):
            check_exists = get_user_by_email(data['email'])
            check_exists2 = get_user_by_username(data['username'])
            if check_exists:
                return {'Status': 409, 'Message':"Email already exists!"},409
            if check_exists2:
                return {'Status': 409, 'Message':"Username already exists!"},409
            isAdmin = False
            create_user = User(data['firstname'],
							data['lastname'],  
							data['email'],
                            data['phoneNumber'],
                            data['username'],
							data['password'],
							isAdmin)
            create_user.add_new_user()
            user = create_user.user_data()

            return {'Status': 201, 'Message': "User registered successfully", 'User': user}, 201
        return new_user_validator(data)