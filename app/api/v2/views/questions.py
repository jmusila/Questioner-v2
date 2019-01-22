#Third party imports
from flask_restplus import Resource
from flask import request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.common.validators import admin_required
from app.api.v2.db_config import cur
from app.api.v2.models.questions import Question
from app.api.v2.views.expect import QuestionModel
from .helpers import get_user_by_email

new_qsn = QuestionModel().questions
v2 = QuestionModel().v2