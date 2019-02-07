#Third party imports
from flask_restplus import Resource
from flask import request, abort
from werkzeug.security import check_password_hash 


#Local imports
from app.api.v2.models.user import User
from app.api.v2.views.expect import UserRegister, UserLogin
from app.api.common.validators import valid_email, new_user_validator
from app.api.v2.db_config import conn
from .helpers import get_user_by_email, get_user_by_username
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

cur = conn.cursor()

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
            if len(data['password']) < 6:
                return {"Status":400, 'Message': 'Password should be at least 6 characters'}, 400
            create_user.add_new_user()
            user = create_user.user_data()

            return {'Status': 201, 'Message': "User registered successfully", 'User': user}, 201
        return new_user_validator(data)
        
@v2.route('/login')
class Login(Resource):

    @v2.expect(new_user)
    def post(self):
        '''Login to Questioner '''
        data = request.get_json()
        email = "".join(data['email'].split())
        password = "".join(data['password'].split())
        if email  == '':
            msg = 'The email field can not be empty'
            return {"Status":400, "Message":msg},400
        if password=='':
            msg = 'The password field can not be empty'
            return {"Status":400, "Message":msg},400
        current_user = get_user_by_email(email)
        if not current_user: 
            return {"Status":400, 'Message': 'User {} does not exist'.format(data['email'])}, 400
        if not check_password_hash(current_user[6], password):
            return {"Status":400, 'Message': "The password is incorrect"}, 400
        access_token = create_access_token(identity = data['email'])
        return {"Status": 200, "access_token": access_token}, 200