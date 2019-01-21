""" Base tests module """

import unittest
import json

# Local application imports
from app.apps import create_app
from app.api.v2.db_config import create_tables, drop_all


config_name = "testing"
app = create_app(config_name)

class Settings(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        create_tables()


    def tearDown(self):
        drop_all()