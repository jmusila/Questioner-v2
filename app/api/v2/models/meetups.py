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
   
    """ Method creating a meetup """
    def add_new_meetup(self):
        meetup = """ INSERT INTO meetups (location, images, title, happeningOn, tags, time_added) 
        VALUES ('{}','{}','{}','{}','{}', '{}') """\
        .format(self.location, self.images, self.title, self.tags, self.happeningOn, self.time_added)
        cur.execute(meetup)
        conn.commit()

    def meetup_data(self):
        return dict(location =self.location, 
                    images = self.images,
                    title = self.title,
                    tags = self.tags,
                    happeningOn = self.happeningOn,
                    time_added = self.time_added)

                    