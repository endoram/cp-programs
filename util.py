import subprocess
import time
import os

# Variables
usr = os.getlogin()

# Sleeper function
def SleepTime():
	time.sleep(1)

def pass_max_days():
	''' This fuction changes PASS_MAX_DAYS

    :param: param1: no parameters
	:returns: error
	'''
	print("********************************")
	print("***  Changing PASS_MAX_DAYS  ***")
	print("********************************")

	subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
	print("[Done]")
	time.sleep(1)

def pass_min_days():
	''' This fuction changes PASS_MIN_DAYS

	    :param: param1: no parameters
		:returns: error
	'''
	print
	print("********************************")
	print("***  Changing PASS_Min_DAYS  ***")
	print("********************************")

while True
	try
		subprocess.call(["sudo", "sed", "-i", '161s/.*/PASS_MIN_DAYS	15/', "login.defs"])
		print("[Done]")
		time.sleep(1)
	break
	except: Value.Error:
		print("Something went wrong.")


# Lists all home directory contents
def search_home():
	print("     Listing /home"
	subprocess.call(["ls", "/home"])
	SleepTime()

# Lists user's home directory contents
def search_user_home():
	print("     Listing home of %s" %usr)
	subprocess.call(["ls", "/home/%s"%usr])
	SleepTime()

# Lists user's desktop directory
def search_user_desktop():
	print("     Listing %s's Desktop"%usr)
	subprocess.call(["ls", "/home/%s/Deskto"%usr])
	SleepTime()
