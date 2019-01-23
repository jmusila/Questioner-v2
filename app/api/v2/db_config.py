"""
This file contains the database configurations and its common operations
"""

# Standard library imports
import os 
import psycopg2


config_name = os.getenv('APP_SETTINGS')
development_url = os.getenv('Dev_URL')
testing_url = os.getenv('Test_URL')
production_url = os.getenv('DATABASE_URL')
conn = psycopg2.connect(development_url)
try:
    """Putting the connection in try """
    if config_name == 'development':
        conn = psycopg2.connect(development_url)
    if config_name == 'testing':
        conn = psycopg2.connect(testing_url)
    if config_name == 'production':
        conn = psycopg2.connect(production_url)
except BaseException:
    print("Database not connected!")

cur = conn.cursor()

def create_tables():
    """
    A fucntion to create all the tables
    """
    queries = tables()
    for quey in queries:
        cur.execute(quey)
    conn.commit()

def create_admin():
    firstname = 'admin'
    lastname = 'super'
    email = 'admin@super.com'
    phoneNumber = '07989898999'
    username = 'Asuper'
    password = generate_password_hash('isAdmin')
    isAdmin = 'True'
    time_created = datetime.now()

    cur.execute("SELECT * FROM users WHERE email='{}';".format(email))
    user = cur.fetchone()
    if not user:
        user = """ INSERT INTO users (firstname, lastname, email, phoneNumber, username, password, isAdmin, time_created) 
        VALUES ('{}','{}','{}','{}','{}', '{}' , '{}' , '{}') """\
        .format(firstname, lastname, email, phoneNumber, username, password, isAdmin, time_created)
        cur.execute(user)
        conn.commit() 

def drop_all():
    """
    Method for droping all the database tables
    """
    cur.execute("DROP TABLE IF EXISTS questions CASCADE")
    cur.execute("DROP TABLE IF EXISTS users CASCADE")
    cur.execute("DROP TABLE IF EXISTS comments CASCADE")
    cur.execute("DROP TABLE IF EXISTS meetups CASCADE")
    cur.execute("DROP TABLE IF EXISTS responses CASCADE")
    cur.execute("DROP TABLE IF EXISTS votes CASCADE")
    conn.commit()


def tables():
    """
    Method for defining all the database tables
    """

    questions = """
        CREATE TABLE IF NOT EXISTS questions(id serial PRIMARY KEY,
        user_id int,
        meetup_id int,
        votes int,
        title varchar,
        body varchar,
        time_added timestamp);
        """

    users = """
        CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,
        firstname varchar,
        lastname varchar,
        email varchar,
        phoneNumber varchar,
        username varchar,
        password varchar,
        isAdmin boolean,
        time_created timestamp);       
        """

    tokens = """
        CREATE TABLE IF NOT EXISTS tokens(id serial PRIMARY KEY,
        token varchar);
        """

    comments = """
        CREATE TABLE IF NOT EXISTS comments(id serial PRIMARY KEY,
        user_id int,
        question_id int,
        comment varchar,
        time_added timestamp);
        """

    meetups = """
        CREATE TABLE IF NOT EXISTS meetups(id serial PRIMARY KEY,
        location varchar,
        images varchar,
        title varchar,
        tags varchar,
        happeningOn varchar,
        time_added timestamp);
        """

    responses = """
        CREATE TABLE IF NOT EXISTS responses(id serial PRIMARY KEY,
        meetup_id int,
        user_id int,
        response varchar);
        """

    votes = """
        CREATE TABLE IF NOT EXISTS votes(id serial PRIMARY KEY,
        question_id int,
        user_id int,
        votes int);
        """

    queries = [questions, users, comments, meetups, responses, tokens, votes]

    return queries








