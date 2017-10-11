
import util
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

print ("********************************")
print ("*        Bee-Secure 1.0        *")
print ("*   Made By Spencer McConnell  *")
print ("********************************")

os.chdir("/etc")
subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
print

util.pass_max_days()
print

util.pass_min_days()
print

util.pass_warn_age()
print

util.disable_guest_login()
print

util.enable_firewall()
print

util.search_home()
print

util.search_user_home()
print

util.search_user_desktop()
print
