#Third party imports
from flask_restplus import Resource
from flask import request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.v2.db_config import cur
from app.api.v2.models.meetups import Meetup
from app.api.v2.views.expect import MeetupModel

new_meetup = MeetupModel().meetups
v2 = MeetupModel().v2


@v2.route('')
class AddMeetup(Resource):
    @v2.expect(new_meetup, validate = True)
    @v2.doc(security='apikey')
    @jwt_required
    def post(self):
        '''Add a new meetup'''
        data = request.get_json()
        create_mtup = Meetup(data['location'],
						data['images'],
						data['title'],
						data['happeningOn'],
						data['tags'])
        create_mtup.add_new_meetup()
        mtup = create_mtup.meetup_data()

        return {'Status': 201, 'Message': "Meetup added successfully", 'Meetup': mtup}, 201