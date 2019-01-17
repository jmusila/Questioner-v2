import re



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



