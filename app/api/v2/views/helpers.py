# Local imports
from app.api.v2.db_config import conn

# database connection
cur = conn.cursor()


def get_user_by_email(email):
    """
    Fetch a single user by email
    """
    cur.execute("SELECT * FROM users WHERE email='{}';".format(email))
    user = cur.fetchone()
    return user

def get_user_by_username(username):
    """
    Fetch a single user by thier username
    """
    cur.execute("SELECT * FROM users WHERE username='{}';".format(username))
    user = cur.fetchone()
    return user