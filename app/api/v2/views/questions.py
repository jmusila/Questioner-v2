#Third party imports
from flask_restplus import Resource
from flask import request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.v2.db_config import cur
from app.api.v2.models.questions import Question
from app.api.v2.views.expect import QuestionModel
from .helpers import get_user_by_email

new_qsn = QuestionModel().questions
v2 = QuestionModel().v2

@v2.route('/<int:id>/questions')
class AddQuestion(Resource):
    @v2.expect(new_qsn, validate = True)
    @v2.doc(security='apikey')
    @jwt_required
    def post(self, id):
        '''Add a new question'''
        user = get_user_by_email(get_jwt_identity())
        if user:
        	user_id = user[0]
        votes = 0
        cur.execute("SELECT * FROM meetups WHERE id='{}';".format(id))
        mtup = cur.fetchone()
        if not mtup or mtup[0] != id:
            msg = 'Meetup with that id does not exist'
            return {"Message":msg},404
        meetup_id = mtup[0]
        data = request.get_json()
        create_qsn = Question(user_id, 
        				meetup_id,
        				votes,
						data['title'],
						data['body'])
        create_qsn.add_question()
        qsn = create_qsn.question_data()

        return {'Status': 201, 'Message': "Question posted successfully", 'Question': qsn}, 201