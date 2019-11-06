import json

#local imports
from .base_test import Settings

meetups_url = "api/v2/meetups/upcoming"

class TestMeetup(Settings):
    meetup =   {
            "location": "PAC",
          "images": "image.jpg",
          "title": "Python",
          "tags": "me, you",
        "happeningOn": "14/4/2019"
    } 

    def test_post_meetup(self):
        """
        Test post a meetup
        """
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['message'], 'meetup added successfully')
        self.assertEqual(res.status_code, 201)


    def test_get_single_meetup(self):
        """Test API can get a single meetup by using it's id."""
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        rv1 = self.app.get('api/v2/meetups/upcoming/1')
        data = json.loads(rv1.data.decode())
        self.assertEqual(rv1.status_code, 200)
        self.assertIn('PAC', str(rv1.data))

    def test_get_all_meetups(self):
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        res1 = self.app.get('api/v2/meetups/upcoming')
        data = json.loads(res1.get_data().decode())
        self.assertEqual(res1.status_code, 200)
        self.assertIn('Python', str(res1.data))

    def test_xdelete_meetup(self):
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        res1 = self.app.delete('api/v2/meetups/upcoming/1', data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        data = json.loads(res1.get_data().decode())
        self.assertEqual(res1.status_code, 200)
        result = self.app.get('/api/v2/meetus/upcoming/1')
        self.assertEqual(result.status_code, 404)

        