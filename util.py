import subprocess
import time
import os


usr = os.getlogin()


def SleepTime():
	time.sleep(1)


def pas_max_days():
	print "********************************"
	print "*   Changing PASS_MASS_DAYS    *"
	print "********************************"

	subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
	print "[Done]"
	time.sleep(1)
	

def pas_min_days():
	print
	print "********************************"
	print "*    Changing PASS_Min_DAYS    *"
	print "********************************"

	subprocess.call(["sudo", "sed", "-i", '161s/.*/PASS_MIN_DAYS	15/', "login.defs"])
	print "[Done]"
	time.sleep(1)

def search_home():
	print "     Listing /home"
	subprocess.call(["ls", "/home"])
	SleepTime()

def search_user_home():
	print "     Listing home of %s"%usr
	subprocess.call(["ls", "/home/%s"%usr])
	SleepTime()

def search_user_Desktop():
	print "     Listing %s's Desktop"%usr
	subprocess.call(["ls", "/home/%s/Deskto"%usr])
	SleepTime()
<<<<<<< Updated upstream
=======

def search_user_Documents():
	print "     Listing %s's Desktop"%usr
	subprocess.call(["ls", "/home/%s/Deskto"%usr])
	SleepTime()
>>>>>>> Stashed changes
