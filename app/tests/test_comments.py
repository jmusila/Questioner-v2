import json

#local imports
from .base_test import Settings

question_url = "api/v2/meetups/1/questions"
meetups_url = "api/v2/meetups/upcoming"
comments_url = "api/v2/questions/1/comments"

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
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        token = self.give_token()
        res = self.app.post(question_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.post(comments_url,
                            data=json.dumps(self.comment),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], "Comment posted successfully")
        self.assertEqual(res.status_code, 201)  

    def test_get_all_comments(self):
        token = self.give_token()
        res = self.app.post(comments_url,
                            data=json.dumps(self.comment),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        res1 = self.app.get('api/v2/questions/1/comments')
        data = json.loads(res1.get_data().decode())
        self.assertEqual(res1.status_code, 200)
        self.assertIn('This is my comment', str(res1.data))