#Third party imports
from flask_restplus import Resource
from flask import request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.v2.db_config import cur
from app.api.v2.models.meetups import Meetup
from app.api.v2.views.expect import MeetupModel
from .helpers import get_meetup_by_id
from app.api.common.validators import new_meetup_validator
from .helpers import get_user_by_email, check_meetup_exists

new_meetup = MeetupModel().meetups
v2 = MeetupModel().v2


@v2.route('')
class AddMeetup(Resource):
    @v2.expect(new_meetup, validate = True)
    @v2.doc(security='apikey')
    @jwt_required
    def post(self):
        '''Add a new meetup'''
        user = get_user_by_email(get_jwt_identity())
        if user[7] != True:
            msg ='Access denied! Please contact the admin'
            return {'Message': msg}, 401
        data = request.get_json()
        check_exists = check_meetup_exists(data['title'], data['happeningOn'], data['location'])
        if check_exists:
                return {'status': 409, 'message':"meetup already exists!"},409
        if not new_meetup_validator(data):
            create_mtup = Meetup(data['location'],
        					data['images'],
        					data['title'],
        					data['happeningOn'],
        					data['tags'])
            create_mtup.add_new_meetup()
            mtup = create_mtup.meetup_data()
            return {'status': 201, 'message': "meetup added successfully", 'Meetup': mtup}, 201
        return new_meetup_validator(data)

    def get(self):
        """
        Get all meetups
        """
        cur.execute(
            "SELECT * FROM meetups")
        meetups = cur.fetchall()
        all_meetups = []
        for item in meetups:
            format_meetup = {'meetup_id': item[0],
                        'location': item[1],
                        'images': item[2],
                        'title': item[3],
                        'happeningOn': item[4],
                        'tags': item[5],
                        'time_added':str(item[6])}
            all_meetups.append(format_meetup)
        if len(all_meetups) < 1:
            res= {"status":404,"message":"mhere are no meetups at the moment"},404
            return res
        return {"status": 200, "data": all_meetups}, 200 

@v2.route('/<int:id>')
class MeetupDetails(Resource):
    def get(self, id):
        """
        Get a single meetup
        """
        meetup = get_meetup_by_id(id)
        if not meetup:
            msg = 'meetup with that id does not exist'
            return {"Status":404, "Message":msg},404
        format_meetup = {'meetup_id': meetup[0],
                    'location': meetup[1],
                    'images': meetup[2],
                    'title': meetup[3],
                    'happeningOn': meetup[4],
                    'tags': meetup[5],
                    'time_added':str(meetup[6])}
        return {"status": 200, "meetup": format_meetup}, 200

    @v2.doc(security='apikey')
    @jwt_required
    def delete(self, id):
        """
        Admin delete a meetup
        """
        user = get_user_by_email(get_jwt_identity())
        if user[7] != True:
            msg ='access denied! please contact the admin'
            return {'message': msg}, 401
        meetup = get_meetup_by_id(id)
        if not meetup:
            msg = 'meetup with that id does not exist'
            return {"status":404, "message":msg},404
        cur.execute("DELETE FROM meetups WHERE id={};".format(id))
        msg = 'meetup deleted successfully!'
        return {'message': msg}, 200
        