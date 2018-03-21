#!/usr/bin/env python3

from tkinter import *						#import window manager
import re, time, threading, os, wave, subprocess		#import re to orginse the incoming string, time to keep track of time and threading to do more then 1 thing
from tkinter import messagebox					#Import this to help shutdown the whole  script
import fileinput, shlex


global switch, z, complete, totalpoints, f
switch = 1

complete = 0
totalscored = 0
totalpoints = 0

currentuser = os.getlogin()

f = 0	#This var is used to check inputs see playwinsound()
x = 0
z = 0

def readfile():
	global complete, totalpoints, totalscored, input, hms, input2

	#The next four lines opens the output from scoregen.py and puts it into a readable varible
	os.chdir("/home/{0}/cyberpatriot".format(currentuser))
	file = open("output.txt")
	input = file.readlines()		#Reads the lines
	input = str(input)			#Puts into var input
	input = re.sub("\D", "", input)		#Creates finnal output of 100110101
	#print(input)

	input1 = input                          #Creates dublicate of the input
	totalscored = input1.strip("0")         #Strips all 0s
	totalscored = len(totalscored)          #Gets lenght of all scored things(This tells me how many issues need fixing)
	#print(totalscored)

	#The next part finds out how much each point should score
	hms = 100/totalscored
	print(hms)

	input2 = input                  #Crating another dublicate

def frameit():
	global complete, totalpoints, totalscored, z, outof1, points1, hms
	global rootlogin1, protocal1, x11forwarding1, addadmin1, addprogram1, addjams1
	z = z + 1

	#The next 2 lines creates the title and puts my name in the corner
	title = Label(root, font="Helvetica 44 bold", text="CyberPatriot Special Ubuntu 16 Round", background="white").grid(row=2, column=1)
	tradmark = Label(root, font="Helvetica 10 bold", text="Spencer McConnell").place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

	#This block creates the total points earned
	points1 = StringVar()
	points1.set("{0} out of 100 points received".format(int(totalpoints)))
	points = Label(root, font="Helvetica 33 bold", textvariable=points1, background="white").grid(row=3, column=1)

	#Creates the label that tells you all the valuns you need to fix
	outof1 = StringVar()
	outof1.set("{0} out of {1} scored security issues fixed.".format(complete, totalscored))
	outof = Label(root, font=22, textvariable=outof1).grid(row=4, column=0)

	#Creates root login label
	rootlogin1 = StringVar()
	rootlogin1.set("")
	rootlogin = Label(root, font=23, textvariable=rootlogin1, background="white").grid(row=5, column=0)

	#Creates the protocal label
	protocal1 = StringVar()
	protocal1.set("")
	protocal = Label(root, font=23, textvariable=protocal1, background="white").grid(row=6, column=0)

	#Creates label for X11Forwarding
	x11forwarding1 = StringVar()
	x11forwarding1.set("")
	x11forwarding = Label(root, font=23, textvariable=x11forwarding1, background="white").grid(row=7, column=0)

	#Label for creating admin account deloortteg
	addadmin1 = StringVar()
	addadmin1.set("")
	addadmin = Label(root, font=23, textvariable=addadmin1, background="white").grid(row=8, column=0)

	#Making label for when addprogram scores
	addprogram1 = StringVar()
	addprogram1.set("")
	addprogram = Label(root, font=23, textvariable=addprogram1, background="white").grid(row=9, column=0)

	addjams1 = StringVar()
	addjams1.set("")
	addjams = Label(root, font=23, textvariable=addjams1, background="white").grid(row=10, column=0)


def playsoundwin():
	global complete, totalpoints, totalscored, input, hms, input2, f

	complete = complete + 1                 #Add 1 point to total of completed fixes
	totalpoints = totalpoints + hms         #Add points to the total of pints

	input3 = list(input2)   #Change input 2 into a list called input3
	input3[f] = 0           #Changes the 1 to 0 (meaning it will not check to score anymore)
	input3 = str(input3)                    #Sets input back to string
	input2 = re.sub("\D", "", input3)



	#We can put the next to vars here because we have to re set them each time a point is scored
	outof1.set("{0} out of {1} scored security issues fixed.".format(complete, totalscored))
	points1.set("{0} out of 100 points received".format(int(totalpoints)))

	root.update()
	#This function plays the mario sound when point is earned
	os.chdir("/home/{0}/cyberpatriot".format(currentuser))
	subprocess.call(["mpg123", "scoredapoint.mp3"])


def messitup():
	#This function sets all the scored topics to the wrong setting
	print("Messing up the image")

	check = input2[0]	#checks to see if its scored
	check = str(check)	#changes it to a string
	if(check == "1"):		#if it is scored
		os.chdir("/etc/ssh")	#Goes to that directory
		with fileinput.FileInput("sshd_config", inplace=True) as file:						#Reads file
			for line in file:print(line.replace("PermitRootLogin no", "PermitRootLogin yes"), end="")	#Replaces right with wrong


	#Repeats but checks for another thing
	check = input2[1]
	check = str(check)
	if(check == "1"):
		os.chdir("/etc/ssh")
		with fileinput.FileInput("sshd_config", inplace=True) as file:
			for line in file:print(line.replace("Protocal 2", "Protocal 1"), end="")


        #Repeats but checks for another thing
	check = input2[2]
	check = str(check)
	if(check == "1"):
		os.chdir("/etc/ssh")
		with fileinput.FileInput("sshd_config", inplace=True) as file:
			for line in file:print(line.replace("X11Forwarding no", "X11Forwarding Yes"), end="")



def startcard():
	#This function checks for everything that is scored
	global complete, totalpoints, totalscored, outof1, input, points1, input2, f
	global rootlogin1, x11forwarding1, addadmin1, addprogram1, addjams1

	print(input2)

	check = input2[0]	#Grabes 0th term of input2
	check = str(check)	#changes it to a string
#	print(check)
	if check == "1":	#If it is 1:
	#	print("Hey")
		os.chdir("/etc/ssh")		#Changes dirctory to ssh folder
		if "PermitRootLogin no" in open("sshd_config").read():		#If PRL is set to no in sshd_config
			print("Scoring PermitROotLogin no")

			#Update the vars on the screen
			rootlogin1.set("Root Login Disabled - {0}".format(int(hms)))	#Shows up in completed tasks

			f = 0
			playsoundwin()		#Goes to function playsoundwin()


	#Repete process but with the next item
	check = input2[1]
	check = str(check)
#	print(check)
	if check == "1":
	#	print("Hey")
		os.chdir("/etc/ssh")
		if "Protocal 2" in open("sshd_config").read():
			print("Scoring Protocal 1 to 2")

			protocal1.set("Protocal changed from 1 to 2 - {0}".format(int(hms)))

			f = 1
			playsoundwin()

	#Repeats again but with the next item
	check = input2[2]
	check = str(check)
	if check == "1":
		os.chdir("/etc/ssh")
		if "X11Forwarding no" in open("sshd_config").read():
			print("Scoring X11Forwarding no")

			x11forwarding1.set("X11Forwarding set to no - {0}".format(int(hms)))

			f = 2
			playsoundwin()

	#Repeats again but with the next thing
	check = input2[3]
	check = str(check)
	if check == "1":
		command1 = "grep -Po '^sudo.+:\K.*$' /etc/group"		#This command checks all admins
		os.chdir("/etc")
		a = subprocess.check_output(shlex.split(command1))
		if "deloortteg" in str(a):				#If his name is in the result of command
			print("Scoring admin DeloorTteg was added")

			addadmin1.set("Added admin DeloorTteg - {0}".format(int(hms)))

			f = 3
			playsoundwin()


	check = input2[4]
	check = str(check)
	if check == "1":
		command1 = "dpkg --list"
		a = subprocess.check_output(shlex.split(command1))
		if "stellarium" in str(a):
			print("Scoring added program Stellarium")

			addprogram1.set("Added program Stellarium - {0}".format(int(hms)))

			f = 4
			playsoundwin()



	check = input2[5]
	check = str(check)
	if check == "1":
		command1 = "grep '/bin/bash' /etc/passwd"
		a = subprocess.check_output(shlex.split(command1))
		if "jams"in str(a):
			print("Scoring for user jams added")

			addjams1.set("Added user jams - {0}".format(int(hms)))

			f = 5
			playsoundwin()


	root.after(1000, startcard)		#This makes it so every 1000 milisecdends it starts the startcard function




def callback():
	#This function makes it so when you hit the x button in the top left it ask if you really want to quit
	if messagebox.askokcancel("Quit", "Do you want to quit?"):		#Asks the question
		root.destroy()							#If you hit quit it destroys the window(quiting the window)


root = Tk()						#Creates the window
root.title("Ubuntu 16 scorecard")			#Sets title
root.config(background="white")				#Sets the backfround of the window
root.after(3000, startcard)				#This goes to the starcard function when the root.mainloop starts


readfile()						#This line goes to read file to read the output.txt file

messitup()

frameit()						#Goes to the frameit function creating the things displayed onthe screen

root.mainloop()						#Displays the main window
