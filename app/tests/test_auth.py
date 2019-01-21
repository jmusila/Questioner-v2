import unittest
import json

#local imports
from .base_test import Settings

class TestUser(Settings):
    register ={
          "lastname": "musila",
          "firstname": "jonathan",
          "email": "test@gmail.com",
          "password": "123jonathan",
          "phoneNumber": "0798989870",
          "username": "jmusila"
    }
    registered ={
          "lastname": "musila",
          "firstname": "jonathan",
          "email": "test2@gmail.com",
          "password": "123jonathan",
          "phoneNumber": "0798969867",
          "username": "jmusila"
    }
    regist ={
          "lastname": "dummy",
          "firstname": "jonathan",
          "email": "....@....com",
          "password": "123jonathan",
          "phoneNumber": "0798989898",
          "username": "dummy2"
    }

    login = {
          "email": "test@gmail.com",
          "password": "123jonathan"
    }
    def test_1signup(self):
        """
        Test register a user
        """
        res = self.app.post('api/v2/auth/signup', data=json.dumps(self.register), content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], 'User registered successfully')
        self.assertEqual(res.status_code, 201)

    def test_login(self):
        """Test user login."""
        self.app.post('api/v2/auth/signup', data=json.dumps(self.register), content_type='application/json')
        res = self.app.post('api/v2/auth/login', data=json.dumps(self.login), content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)


    def test_signup_twice_with_same_email(self):
        """
        Test signup twice
        """
        self.app.post('api/v2/auth/signup', data=json.dumps(self.register), content_type='application/json')
        res = self.app.post('api/v2/auth/signup', data=json.dumps(self.register), content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], 'Email already exists!')
        self.assertEqual(res.status_code, 409)

    def test_signup_twice_with_same_username(self):
        """
        Test signup twice
        """
        self.app.post('api/v2/auth/signup', data=json.dumps(self.register), content_type='application/json')
        res = self.app.post('api/v2/auth/signup', data=json.dumps(self.registered), content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], 'Username already exists!')
        self.assertEqual(res.status_code, 409)
