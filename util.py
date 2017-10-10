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

	'''
	print("********************************")
	print("***  Changing PASS_MAX_DAYS  ***")
	print("********************************")

	subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
	print("[Done]")
	SleepTime()

def pass_min_days():
	#This fuction changes PASS_MIN_DAYS

	print
	print("********************************")
	print("***  Changing PASS_MIN_DAYS  ***")
	print("********************************")
	print ("[Done]")


#while
#	try
#		subprocess.call(["sudo", "sed", "-i", '161s/.*/PASS_MIN_DAYS	15/', "login.defs"])
#		print("[Done]")
#		time.sleep(1)
#	break
#	except: Value.Error:
#		print("Something went wrong.")

# Lists all home directory contents
def search_home():
	print("     Listing /home")
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
	subprocess.call(["ls", "/home/%s/Desktop"%usr])
	SleepTime()

def search_user_Documents():
	print "     Listing %s's Desktop"%usr
	subprocess.call(["ls", "/home/%s/Desktop"%usr])
	SleepTime()
