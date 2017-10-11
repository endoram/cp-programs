
import subprocess
import time
import os

# Variables
usr = os.getlogin()

# Sleeper function
def SleepTime():
	time.sleep(1)

def pass_max_days():
	#This fuction changes PASS_MAX_DAYS to 35
	print("Changing PASS_MAX_DAYS to 35")
	subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
	print("[Done]")
	SleepTime()

def pass_min_days():
	#This fuction changes PASS_MIN_DAYS to 17
	print("Changing PASS_MIN_DAYS to 17")
	subprocess.call(["sudo", "sed", "-i", '161s/.*/PASS_MIN_DAYS	15/', "login.defs"])
	print ("[Done]")

def pass_warn_age():
	#This function changes PASS_WARN_AGE to 7
	print("Chaning PASS_WARN_AGE to 7")
	subprocess.call(["sudo", "sed", "-i", '162s/.*/PASS_WARN_AGE	7/', "login.defs"])
	print("[Done]")

def disable_guest_login():
	#This fuction diables the guest login
	print("Disabling guest login")
	os.chdir("/usr/share/lightdm/lightdm.conf.d")
	subprocess.call(["sudo", "sed", "-i", '3s/.*/allow-guests=false/', "50-ubuntu.conf"])
	print("[Done]")
	

def enable_firewall():
	#This funtion turns on the firewall
	print("Enabling firewall")
	subprocess.call(["sudo", "ufw", "enable"])
	print("[Done]")

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
