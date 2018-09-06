from .absence import Absence


class MessageController(object):
    '''
    Formats
    !attendance month day
    !attendance month day username
    !attendance month day ... username
    
    Required
    !attendance
    month
    day

    Optional
    username

    month day - can repeated as many times as needed with optional username
    '''

    months = {'january': 31, 'february': 29, 'march': 31,
              'april': 30, 'may': 31, 'june': 30,
              'july': 31, 'august': 31, 'september': 30,
              'october': 31, 'november': 30, 'december': 31}

    def create_absence(self, message):
        split_message = message.content.split(' ')

        if len(split_message) < 3:
            return ["Please use a proper format or " \
                   "'!help attendance' for more information."]

        absences = []
        if len(split_message) % 2 == 0:
            absences = self.parse_dates(split_message[1:-1],
                                        split_message[-1].lower())
        else:
            absences = self.parse_dates(split_message[1:],
                                        message.author.display_name.lower())

        return absences

    def parse_dates(self, date_list, username):
        absences = []
        try:
            for i in range(0, int(len(date_list) / 2)):
                absence = Absence(username,
                                  self.validate_month(date_list[i * 2]),
                                  self.validate_day(date_list[i * 2],
                                                    date_list[(i * 2) + 1]))

                if absence.is_valid():
                    absences.append(absence)
                else:
                    absences.append('{0} {1} is not a valid date'.format(date_list[i * 2], 
                                                                         date_list[(i * 2) + 1]))
        except Exception as e:
            print(e)
            absences = []

        return absences

    def validate_month(self, month):
        return month.capitalize() if month.lower() in self.months.keys() else None

    def validate_day(self, month, day):
        try:
            day_limit = self.months.get(month.lower())
            return day if 0 < int(day) <= day_limit else None
        except (ValueError, TypeError):
            return None
