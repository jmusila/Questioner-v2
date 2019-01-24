"""
This will contain the base tests configuration.
Thi will be reused/imported in almost all the tests.
"""

import unittest
import json

# Local application imports
from app.apps import create_app
from app.api.v2.db_config import create_tables, drop_all


config_name = "testing"
app = create_app(config_name)

login_url = "/api/v2/auth/login"
signup_url = "/api/v2/auth/signup"


class Settings(unittest.TestCase):

	login_data = {
	"email": "admin@super.com",
	"password": "isAdmin"
	}

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		create_tables()

	def give_token(self):
		login = self.app.post(login_url, data=json.dumps(self.login_data), content_type='application/json')	
		login_data = json.loads(login.data.decode())
		return login_data["access_token"]
        