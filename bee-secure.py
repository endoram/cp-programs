
import utilities
import os
import subprocess


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


