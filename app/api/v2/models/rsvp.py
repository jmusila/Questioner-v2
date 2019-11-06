from datetime import datetime

class Responds:
    """ Respond constructor """

    def __init__(self, r_id, meetup_id, topic, status):
        self.r_id = r_id
        self.meetup_id = meetup_id
        self.topic = topic
        self.status = status

    """ Method for getting single comment   """
    def get_single_response(self, r_id):
        pass


