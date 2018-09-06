# AttendanceBot

---SETUP---

This project uses Python 3.6 due to discord api wrapper dependencies.

Install Python from https://www.python.org/downloads/

Check to make sure Python 3.6 is your default by using command line and using 'python -V'

If you have Python 2.X already installed either change your PATH environment variable to point to 3.6 or use python3 commands

Check to see if pip was installed alongside Python 3.6 by using the command 'pip -V'

You'll want to make sure that it's also pointing to Python 3.6 at the end of the response

Install virtualenv using 'pip install virtualenv'

Once you've pulled down the project from github create a virtual env for the project by using the command 'virtualenv venv' inside the project root directory

Navigate to ./AttendanceBot/venv/Scripts and run the activate command, this will start the virtual environment

Navigate back to the project root directory and then run 'pip install -r requirements.txt', this will install all the proper dependencies for the project

Now you're ready to start working, the main code is stored inside the src folder

---MAKE SURE YOU DONT COMMIT THE BOT TOKEN---

Always set the bot token in attendancebot.py back to just 'TOKEN'

The token will be stored in the testing discord server so always place back while working on the bot and then remove before committing
