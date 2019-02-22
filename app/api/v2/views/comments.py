#Third party imports
from flask_restplus import Resource
from flask import request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_raw_jwt

#Local imports
from app.api.v2.db_config import cur
from app.api.v2.models.comments import Comment
from app.api.v2.views.expect import CommentModel
from app.api.common.validators import comment_validator
from .helpers import get_user_by_email, get_question_by_id

new_comment = CommentModel().comments
v2 = CommentModel().v2

@v2.route('/<int:id>/comments')
class AddComment(Resource):
    @v2.expect(new_comment, validate = True)
    @v2.doc(security='apikey')
    @jwt_required
    def post(self, id):
        '''Add a new comment'''
        data = request.get_json()
        if not comment_validator(data):
            user = get_user_by_email(get_jwt_identity())
            if user:
                user_id = user[0]
            qsn = get_question_by_id(id)
            if not qsn or qsn[0] != id:
                msg = 'Question with that id does not exist'
                return {"Message":msg},404
            question_id = qsn[0]
            create_comment = Comment(user_id, 
                            question_id,
                            data['comment'])
            create_comment.add_comment()
            cmnt = create_comment.comment_data()

            return {'Status': 201, 'Message': "Comment posted successfully", 'Comment': cmnt}, 201
        return comment_validator(data)

    def get(self, id):
        """
        Get all comments for a specific question
        """
        cur.execute(
            "SELECT * FROM comments WHERE question_id={};".format(id))
        questions = cur.fetchall()
        qsn = get_question_by_id(id)
        all_comments = []
        for item in questions:
            format_comment = {'comment_id': item[0],
                        'user_id': item[1],
                        'question_id': item[2],
                        'comment': item[3],
                        'time_added':str(item[4])}
            all_comments.append(format_comment)
        if not qsn or qsn[0] != id:
            msg = 'Question with that id does not exist'
            return {"Status":404, "Message":msg},404
        if len(all_comments) < 1:
            res= {"Status":404,"Message":"There are no Comments at the moment"},404
            return res
        return {"Status": 200, "data": all_comments}, 200
        