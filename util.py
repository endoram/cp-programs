
# coding: utf-8

import subprocess
import time
import os

# Variables
usr = os.getlogin()

#This is a list of all the things to find(refer to findpackage())
list1 = ["*.png", "*nmap*", "*.mp4", "*.wav", "*rainbow*", "*crack*", "*.mp3", "*hyd*"]


def findpackagev1():
	#This function looks for the files in list1
	z = 0
	a = 0
	print("Searching For files")
	#While loop that goes through and checks every word in list1
	while z <= 6:
		print(list1[a])
		subprocess.call(["sudo", "find", "/home", "-name", list1[a]])
		print("#############################################################")
		a = a + 1
		z = z + 1

# Sleeper function
def SleepTime():
	time.sleep(1)

def bum():
	print("Installing bum")
	subprocess.call(["sudo", "apt-get", "install", "bum"])
	print("[Done]")

def audit():
	#This function installs auditd and enables it
	print("Installing auditd")
	subprocess.call(["sudo", "apt-get", "install", "auditd"])
	print("Turing on auditd")
	subprocess.call(["sudo", "auditctl", "–e", "1"])
	print("[Done]")

def ssh_secure():
	#This function makes ssh not be able to do root login and changes protocal 1 to 2
	os.chdir("/etc/ssh/")
	print("Disabling root login")


def password_policy():
	os.chdir("/etc/pam.d/")
	print("Changing minimum password lenght to 8")
	subprocess.call(["sudo", "sed", "-i", '17s/.*/pam_unix.so minlen=8/', "common-password"])
	print("[Done]")


def set_root_password():
	#This adds a root password
	print("Setting root password")
	subprocess.call(["sudo", "passwd", "root"])
	print("[Done]")


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
	SleepTime()


def pass_warn_age():
	#This function changes PASS_WARN_AGE to 7
	print("Chaning PASS_WARN_AGE to 7")
	subprocess.call(["sudo", "sed", "-i", '162s/.*/PASS_WARN_AGE	7/', "login.defs"])
	print("[Done]")
	SleepTime()


def disable_guest_login():
	#This fuction disables the guest login
	#var_disable_guest is equal to what the gedit file should look like
	var_disable_guest = ['[SeatDefaults]\n', 'greeter-session=unity-greeter\n', 'user-session=ubuntu\n', 'allow-guests=false\n']

	print("Disabling guest login")
	os.chdir("/etc/lightdm/lightdm.conf")

	#Read lightdm.conf set the lines to content
	with open("lightdm.conf") as f:
		content = f.readlines()

	#Check that the file equals var_disable_guest
	if (content == var_disable_guest):
		print("[Checked]")

	# if it does not equal then add the line allow-guests=false
	else:
		subprocess.call(["sudo", "sed", "-i", '/user-session=ubuntu/ a\
		allow-guests=false', "50-ubuntu.conf"])
		#print("[Done]")

	#Read lightdm.conf set the lines to content
	with open("lightdm.conf") as f:
		content = f.readlines()

	#This is a check for the system
	#If content equals var_disable_guest then do nothing
	#Else print failed
	if (content == var_disable_guest):
		print("[Done]")
	else:
		print("[Failed]")
		print(content)

	SleepTime()


def enable_firewall():
	#This funtion turns on the firewall
	print("Enabling firewall")
	subprocess.call(["sudo", "ufw", "enable"])
	print("[Done]")
	SleepTime()


def search_home():
	# Lists all home directory contents
	print("     Listing /home")
	subprocess.call(["ls", "/home"])
	SleepTime()
