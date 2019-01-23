import re
from functools import wraps
from flask_jwt_extended import get_jwt_identity



#Local imports
from app.api.v2.views.helpers import get_user_by_email


def common(expected_payload, data):
    """
    
    The expected payload is the expected data and we compare it 
    to the json data
    """
    for key in data.keys():
        if key not in expected_payload:
            msg = 'The field {} is not required'.format(key)
            return {"Status":400, "Message":msg},400
    for item in expected_payload:
        if item not in data.keys():
            msg = 'Please provide the {} field'.format(item)
            return {"Status":400, "Message":msg},400
    for item, value in data.items():
        if not isinstance(value, int):
            value_without_white_space = "".join(value.split())
            if value_without_white_space == "":
                msg = 'The {} can not be empty'.format(item)
                return {"Status":400, "Message":msg},400

def valid_email(email):
    if not \
    re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$", email):
        msg = 'Please enter a valid email'
        return {'Status':406,"Message":msg},406

def valid_phone_number(phoneNumber):
    if not \
    re.match(r"^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$", phoneNumber):
        msg = 'Please enter a valid phone number'
        return {'Status':406,"Message":msg},406

def new_user_validator(data):
    """
    Validate a new user inputs
    """

    pay_load = ['firstname', 'lastname', 'phoneNumber', 'username', 'email', 'password']
    res = common(pay_load, data)
    if not res:
        for item, value in data.items():
            if not isinstance(value, str):
                msg = 'The {} field is supposed to be a string'.format(item)
                res = {"Status":406,"Message":msg},406
            if item == 'password':
                if len(item) < 8:
                    msg = 'The {} must have atleast eight characters'
                    res= {"Status":406,"Message":msg},406
            if item == 'email':
                res = valid_email(value)
            if item == 'phoneNumber':
                res = valid_phone_number(value)
    return res

def new_meetup_validator(data):

    expected_pay_load = ['location', 'happeningOn', 'images', 'tags', 'title' ]
    res = common(expected_pay_load, data)

    return res


def question_validator(data):
    expected_pay_load = ['title', 'body']
    res = common(expected_pay_load, data)

    return res

def comment_validator(data):
    expected_pay_load = ['comment']
    res = common(expected_pay_load, data)

    return res
    