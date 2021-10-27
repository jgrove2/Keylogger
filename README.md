# Keylogger
 
## What does it do?
The keylogger is a very simple take on a keylogger. It is easily picked up by windows defender which almost instantly deletes the file. However, when it is not instantly deleted due to being labeled as a keylogger by windows it does its job specified by its parameters. The function of this keylogger is to run as a python file collecting the key and time/date of when it was pressed. Every x amount of seconds as specified in the key.py file it will send an email from an input address to an email of an also specified address.
## key.py
This is the main file of the program. Here it uses pynput and threading to update a log file that contains all of the keys pressed on the infected computer. After a specified time it calls the sendEmail() function from the sendEmail.py file.
## sendEmail.py
In this file, it uses smtplib to send emails from google or any specified email host. It constructs a multi-part message that is sent containing the keylog.txt file which has the logs of all keystrokes.