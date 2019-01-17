#Third party imports
from flask_restplus import Resource
from flask import request, abort
from werkzeug.security import check_password_hash 
from .helpers import get_user_by_email
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.v2.models.user import User
from app.api.v2.views.expect import UserRegister, UserLogin
from app.api.common.validators import valid_email, new_user_validator

new_user = UserRegister().users
v2 = UserRegister().v2
login = UserLogin().login
l2 = UserLogin().v2