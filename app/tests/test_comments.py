import json

#local imports
from .base_test import Settings

class TestComment(Settings):
    comment =   {
            "comment": "This is my comment",
    } 

    quiz =   {

          "title": "Python",
          "body": "This is the body of this question"
    }
    meetup =   {
            "location": "PAC",
          "images": "image.jpg",
          "title": "Python",
          "tags": "me, you",
        "happeningOn": "14/4/2019",
        "time_added": "2019-01-15 15:33:24.404035"
    } 

    def test_post_comment(self):
        """
        Test post a comment
        """
        token = self.give_token()
        res = self.app.post("api/v2/meetups/upcoming",
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        token = self.give_token()
        res = self.app.post("api/v2/meetups/1/questions",
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.post("api/v2/questions/1/comments",
                            data=json.dumps(self.comment),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], "Comment posted successfully")
        self.assertEqual(res.status_code, 201)
        