#!/usr/bin/env python

import subprocess
import time
import os


def SleepTime():
	time.sleep(3)
	
#s

subprocess.call(["clear"])
os.chdir("/etc")
usr = os.getlogin()

print usr
print "********************************"
print "*   Problem Fixer Version 1.0  *"
print "*   Made By Spencer McConnell  *"
print "********************************"

print
subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
os.chdir("/etc")

print "********************************"
print "*   Changing PASS_MASS_DAYS    *"
print "********************************"

subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
print "[Done]"
time.sleep(2)


print
print "********************************"
print "*    Changing PASS_Min_DAYS    *"
print "********************************"

subprocess.call(["sudo", "sed", "-i", '161s/.*/PASS_MIN_DAYS	15/', "login.defs"])
print "[Done]"
time.sleep(2)


print
print "Listing /home"
subprocess.call(["ls", "/home"])
SleepTime(2)


print
print "Listing home of %s"%usr
subprocess.call(["ls", "/home/%s"%usr])
SleepTime()


print
print "Listing Do"












