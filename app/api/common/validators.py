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



