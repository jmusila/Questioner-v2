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
    def __init__(self, firstname, lastname, email, phoneNumber, username, password, isAdmin):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = generate_password_hash(password)
        self.isAdmin = isAdmin
        self.time_created = datetime.now()


    """ Method for creating a new user """
    def add_new_user(self):
        user = """ INSERT INTO users (firstname, lastname, email, phoneNumber, username, password, isAdmin, time_created) 
        VALUES ('{}','{}','{}','{}','{}', '{}' , '{}' , '{}') """\
        .format(self.firstname, self.lastname, self.email, self.phoneNumber, self.username, self.password,  self.isAdmin, self.time_created)
        cur.execute(user)
        conn.commit()

    """ Method for user profile """
    def user_data(self):
        return dict(firstname =self.firstname, 
                    lastname = self.lastname,
                    email = self.email,
                    phoneNumber = self.phoneNumber,
                    username = self.username,
                    isAdmin = self.isAdmin)
