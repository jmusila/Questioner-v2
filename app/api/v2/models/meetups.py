from datetime import datetime


#Local imports
from app.api.v2.db_config import conn

cur = conn.cursor()

class Meetup:
    """ Meetups constructor """
    def __init__(self, location, images, title, happeningOn, tags):
        self.time_added = str(datetime.now())
        self.location = location
        self.images = images
        self.title = title
        self.happeningOn = happeningOn
        self.tags = tags
