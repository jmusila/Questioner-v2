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

def get_question_by_id(id):
    cur.execute("SELECT * FROM questions WHERE id='{}';".format(id))
    qsn = cur.fetchone()
    return qsn

def get_meetup_by_id(id):
    cur.execute("SELECT * FROM meetups WHERE id='{}';".format(id))
    mtup = cur.fetchone()
    return mtup

def votes_count(user_id, question_id, votes):
    p_votes = """ INSERT INTO votes (user_id, question_id, votes) 
    VALUES ('{}','{}','{}') """\
    .format(user_id, question_id, votes)
    cur.execute(p_votes)
    conn.commit()
    