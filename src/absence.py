class Absence(object):

    def __init__(self, username, month, day):
        self.username = username
        self.month = month
        self.day = day

    def add_date(self, month, day):
        self.month = month
        self.day = day

    def add_username(self, username):
        self.username = username

    def get_date(self):
        return '{0} {1}'.format(self.month, self.day)
    
    def get_username(self):
        return self.username

    def is_valid(self):
        return True if self.username is not None and self.month is not None \
               and self.day is not None else False
