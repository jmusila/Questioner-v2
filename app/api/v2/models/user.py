"""
A model class for user related operations
"""
#Third party imports
from datetime import datetime
from werkzeug.security import generate_password_hash

#Local imports
from app.api.v2.db_config import conn


# cursor to perform database operations
cur = conn.cursor()