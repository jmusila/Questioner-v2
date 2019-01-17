import unittest
import json

#local imports
from .base_test import Settings

class TestUser(Settings):
    register ={
          "lname": "musila",
          "fname": "jonathan",
          "email": "string@gmail.com",
          "password": "123jonathan"
    }

    def test_signup(self):
        """
        Test register a user
        """
        res = self.app.post('api/v1/auth/signup', data=json.dumps(self.register), content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], 'User registered successfully')
        self.assertEqual(res.status_code, 201)