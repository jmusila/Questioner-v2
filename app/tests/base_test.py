"""
This will contain the base tests configuration.
Thi will be reused/imported in almost all the tests.

"""
# Standard library imports
import unittest
import json

# Local application imports
from app.apps import create_app
from app.api.v2.db_config import create_tables, drop_all

class Settings(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.register ={
            "fname":"jonathan",
            "lname":"musila",
            "isadmin": True,
            "password": "pass"
        }

    def tearDown(self):
        drop_all()