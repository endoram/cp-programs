import os, logging                       #import os to easily change dir import logging to log events and debug
import subprocess, shlex

subprocess.call(["sudo", "pip", "install", "termcolor"])       #Installs termcolor to make it look fun

import util             #Import the other file required to make it work

''' Bee-Secure is a Python script for making Ubuntu VM's more secure for Cyber Patriot teams.
    It was written by Spencer McConnell and is licensed under GPL 3.0.
    Use it at your own risk.
    Requires: util.py
    Created: October 2017
    Python Version: 2.0
'''

usr = spencer
yes = "y"
no = "n"

subprocess.call(["clear"])

print ("********************************")
print ("*        Bee-Secure 1.5        *")
print ("*   Made By Spencer McConnell  *")
print ("********************************")

util.startlog()

uinput = raw_input("Do you want to run your normal script? [y/n]")

if uinput == yes:
    print("Proceding")
    os.chdir("/etc")
    subprocess.call(["sudo", "sed", "-i", '160s/.*/PASS_MAX_DAYS	35/', "login.defs"])
    print

    subprocess.call(["sudo", "pip", "install", "termcolor"])
    from termcolor import colored, cprint

    util.bum()
    print

    util.pammod()
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

    util.findpackagev()
    print

    print("Pick default broswer:")
    subprocess.call(shlex.split("sudo update-alternatives --config x-www-browser"))

    util.users()


else:
    print("Would you like to play a game?")
