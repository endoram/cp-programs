
import utilities
import os
import subprocess


''' Bee-Secure is a Python script for making Ubuntu VM's more secure for Cyber Patriot teams.
    It was written by Spencer McConnell and is licensed under GPL 3.0.
    Use it at your own risk.
    Requires: util.py
    Created: October 2017
    Python Version: 2.0
'''

usr = os.getlogin()

subprocess.call(["clear"])

print "********************************"
print "*        Bee-Secure 1.0        *"
print "*   Made By Spencer McConnell  *"
print "********************************"

os.chdir("/etc")
subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
print


utilities.pas_max_days()

print

utilities.pas_min_days()

print

utilities.search_home()

print

utilities.search_user_home()

print

utilities.search_user_Desktop()

print
