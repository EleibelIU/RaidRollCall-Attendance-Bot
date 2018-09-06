import discord
import asyncio

from src.messagecontroller import MessageController
from src.databasecontroller import DatabaseController
from src.absence import Absence
from datetime import date


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    print('Date')
    print(date.today().strftime("%A - %d %B %Y"))
    print('------------------------')


@client.event
async def on_message(message):
    if message.content.startswith('!attendance'):
        absences = message_controller.create_absence(message)
        inserts = []
        errors = []
        for absence in absences:
            if isinstance(absence, Absence):
                inserts.append(DatabaseController.insert_absence(absence))
            else:
                errors.append(absence)

        await client.send_message(message.channel, merge_inserts_errors(inserts, errors))
    elif message.content.startswith('!list'):
        response = 'Raiders absent:\n'
        absences = DatabaseController.select_absence_where_date()

        if len(absences) > 0:
            for absence in absences:
                response += '{0}\n'.format(absence[0].capitalize())
        else:
            response = 'No absences today.'
        
        await client.send_message(message.channel, response)
    elif message.content.startswith('good bot'):
        await client.send_message(message.channel, 'Thank you {0}'.format(message.author.display_name))
    elif message.content.startswith('bad bot'):
        response = "I'm sorry."
        if message.author.display_name == 'Nohaby':
            response = 'Fuck you Nobaby'
        
        await client.send_message(message.channel, response)

def merge_inserts_errors(inserts, errors):
    response = '\n'
    for insert in inserts:
        response += '{0}\n'.format(insert)
    for error in errors:
        response += '{0}\n'.format(error)
    
    return response

if __name__ == "__main__":
    message_controller = MessageController()
    client.run('TOKEN')
