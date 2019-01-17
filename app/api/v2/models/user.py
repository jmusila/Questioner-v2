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

class User:
    """ User constructor method """
    def __init__(self, fname, lname, email, password, isadmin):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = generate_password_hash(password)
        self.isadmin = False
        self.time_created = datetime.now()

    """ Method for creating a new user """
    def add_new_user(self):
        user = """ INSERT INTO users (fname, lname, email, password, isadmin, time_created) 
        VALUES ('{}','{}','{}','{}','{}', '{}') """\
        .format(self.fname, self.lname, self.email, self.password,  self.isadmin, self.time_created)
        cur.execute(user)
        conn.commit()

    
    """ Method for user profile """
    def user_data(self):

        return dict(fname =self.fname, 
                    lname = self.lname,
                    email = self.email,
                    isadmin = self.isadmin)