from datetime import date

import sqlite3


class DatabaseController(object):

    @staticmethod
    def __create_connection():
        connection = sqlite3.connect('attendance.db')
        cursor = connection.cursor()
        cursor.execute('create table if not exists date (id integer primary key autoincrement, date string);')
        cursor.execute('create table if not exists absence (date_id integer, username string);')

        return connection
    
    @staticmethod
    def insert_absence(absence):
        connection = DatabaseController.__create_connection()
        cursor = connection.cursor()
        # make initial query to see if date is in database
        cursor.execute('select id, date from date where date=?', (absence.get_date(),))
        response = cursor.fetchone()
        id = 0
        # date isn't in database 
        if response is None:
            # insert date then get id
            cursor.execute('insert into date(date) values (?)', (absence.get_date(),))
            connection.commit()
            cursor.execute('select id from date where date=?', (absence.get_date(),))
            id = cursor.fetchone()[0]
        # date is already in database
        else:
            id = response[0]
        
        # make query to see if absence has been logged with date id and username
        cursor.execute('select date_id, username from absence where date_id=? and username=?', (id,
                                                                                                absence.get_username()))
        response = cursor.fetchone()
        inserted = ''
        # absence isn't in database
        if response is None:
            # insert absence into absence table
            cursor.execute('insert into absence(date_id, username) values(?, ?)', (id,
                                                                                   absence.get_username()))
            connection.commit()
            inserted = 'Added absence for {0}: {1}'.format(absence.get_username().capitalize(),
                                                           absence.get_date())
        else:
            inserted = 'Absence for {0} - {1} has already been stored'.format(absence.get_username().capitalize(),
                                                                              absence.get_date())
        
        connection.close()

        return inserted

    @staticmethod
    def select_absence_where_date():
        connection = DatabaseController.__create_connection()
        cursor = connection.cursor()
        cursor.execute('''select a.username 
                          from absence as a 
                          join date as d 
                          on d.id = a.date_id 
                          where d.date=?''', (date.today().strftime('%B %d'),))
        return cursor.fetchall()
