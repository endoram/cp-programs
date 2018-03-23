# -*- coding: utf-8 -*-

import subprocess, logging		#import subprocess to run nix commands import logging to log events and debug
import time
import os, shlex
from termcolor import colored, cprint

# Variables
usr = "spencer"
done = colored('[Done]', 'blue')
level1 = ""


#This is a list of all the things to find(refer to findpackage())
list1 = ["*.png", "*nmap*", "*.mp4", "*.wav", "*rainbow*", "*crack*", "*.mp3", "*hyd*", "*wireshark*", "*.jpeg"]



def startlog():
	'''startlog starts the log file for bee-secure.log'''
	subprocess.call(["sudo", "rm", "bee-secure.log"])

	logging.basicConfig(filename="bee-secure.log",format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	logging.getLogger().setLevel(logging.INFO)
	logging.info("Log is a GO")


	print("0 = Debug")
	print("1 = Info")
	print("2 = Warning")
	print("3 = Error")
	level1 = raw_input("What level of logging:")

	if (level1 == str(0)):
		logging.getLogger().setLevel(logging.DEBUG)
		logging.info("Logging level set to DEBUG")

	if (level1 == str(1)):
		logging.getLogger().setLevel(logging.INFO)
		logging.info("Logging level set to INFO")

	if (level1 == str(2)):
		logging.getLogger().setLevel(logging.WARNING)
		logging.info("Logging level set to WARNING")

	if (level1 == str(3)):
		logging.getLogger().setLevel(logging.ERROR)
		logging.info("Logging level set to ERROR")

	logging.debug("Log level setting complete")


def findpackagev(): 
	#This function looks for the files in list1
	z = 0
	print("Searching For files")
	#While loop that goes through and checks every word in list1
	while z <= 9:
		print(list1[z])
		subprocess.call(["sudo", "find", "/home", "-name", list1[z]])
		text = colored('#########################################################', 'red')
    		print(text)
		z = z + 1
	logging.info("Find package is [DONE]")

# Sleeper function
def SleepTime():
	time.sleep(1)

def bum():
	print("Installing bum")
	subprocess.call(["sudo", "apt-get", "install", "bum"])
	print(done)
	logging.info("Installing bum [DONE]")

def audit():
	#This function installs auditd and enables it
	print("Installing auditd")
	subprocess.call(["sudo", "apt-get", "install", "auditd"])
	print("Turing on auditd")
	subprocess.call(["sudo", "auditctl", "–e", "1"])
	print(done)
	logging.info("Installing auditd [DONE]")

def ssh_secure():
	#This function makes ssh not be able to do root login and changes protocal 1 to 2
	os.chdir("/etc/ssh/")
	#print("Disabling root login")


def password_policy():
	os.chdir("/etc/pam.d/")
	print("Changing minimum password lenght to 8")
	subprocess.call(["sudo", "sed", "-i", '17s/.*/pam_unix.so minlen=8/', "common-password"])
	print(done)
	logging.info("password_policy at pam.d [DONE]")


def set_root_password():
	#This adds a root password
	print("Setting root password")
	subprocess.call(["sudo", "passwd", "root"])
	print(done)
	logging.info("Seting root password [DONE]")


def pass_max_days():
	#This fuction changes PASS_MAX_DAYS to 35
	print("Changing PASS_MAX_DAYS to 35")
	subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
	print(done)


def pass_min_days():
	#This fuction changes PASS_MIN_DAYS to 17
	print("Changing PASS_MIN_DAYS to 17")
	subprocess.call(["sudo", "sed", "-i", '161s/.*/PASS_MIN_DAYS	15/', "login.defs"])
	print (done)


def pass_warn_age():
	#This function changes PASS_WARN_AGE to 7
	print("Chaning PASS_WARN_AGE to 7")
	subprocess.call(["sudo", "sed", "-i", '162s/.*/PASS_WARN_AGE	7/', "login.defs"])
	print(done)


def disable_guest_login():
	#This fuction disables the guest login
	#var_disable_guest is equal to what the gedit file should look like
	var_disable_guest = ['[Seat:*]\n', 'greeter-session=unity-greeter\n', 'user-session=ubuntu\n', 'allow-guests=false\n']

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
		print(done)
	else:
		print("[Failed]")
		print(content)

	SleepTime()


def enable_firewall():
	#This funtion turns on the firewall
	print("Enabling firewall")
	subprocess.call(["sudo", "ufw", "enable"])
	print(done)
	SleepTime()

def pammod():
	#This function installs libcrackpa,
	print("Installing libcrakpam")
	subprocess.call(["sudo", "apt-get", "install", "libpam-cracklib"])
	print(done)

def adduser():
	#This function allows you to add any admins
	text = colored('Type in a user that you want to add to suders:', 'red')
	print(text)
	user = raw_input("")
	subprocess.call(["sudo", "adduser", user, "sudo"])
	print(done)


	#This part allows you to add any user
	text = colored('Type in a user that you want to add as a user:', 'red')
	print(text)
	user = raw_input("")
	subprocess.call(["sudo", "adduser", user])
	print(done)


	#This part allows you to add any user
	text = colored('Type in a user that you want to downgrade to user:', 'red')
	print(text)
	user = raw_input("")
	subprocess.call(["sudo", "deluser", user, "sudo"])
	print(done)


	#This part allows you to add any user
	text = colored('Type in a user that you want to remove:', 'red')
	print(text)
	user = raw_input("")
	subprocess.call(["sudo", "deluser", user])
	print(done)



def users():
	text = colored('Admins:', 'red')
	print(text)
	subprocess.call(shlex.split("grep -Po '^sudo.+:\K.*$' /etc/group"))


	command = "grep '/bin/bash' /etc/passwd"
	print
	text = colored('Users:', 'red')
	print(text)
	subprocess.call(shlex.split(command))
	print


	adduser()
	print










