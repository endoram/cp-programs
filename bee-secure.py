
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
yes = "y"
no = "n"

subprocess.call(["clear"])

print ("********************************")
print ("*        Bee-Secure 1.0        *")
print ("*   Made By Spencer McConnell  *")
print ("********************************")

uinput = raw_input("Do you want to run your normal script? [y/n]")

if uinput == yes:
    print("Proceding")
    os.chdir("/etc")
    subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
    print

    util.logfile()
    print

    util.bum()
    print

    util.audit()
    print

    util.pass_max_days()
    print

    util.pass_min_days()
    print

    util.pass_warn_age()
    print

    #util.disable_guest_login()
    #print

    util.set_root_password()
    print

    #util.password_policy()
    #print

    util.enable_firewall()
    print

    util.findpackagev1()
    print

    util.search_home()
    print

else:
    print("Would you like to play a game?")
