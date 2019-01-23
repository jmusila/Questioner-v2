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