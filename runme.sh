#!/bin/bash

echo "Starting..."

echo "Critical Service?"; read cs		#Get critical Service info
nano users					#Get list of users from user
nano au						#Get list of admins

#Install secirty programs
sudo apt-get install bum
sudo apt-get install libpam-cracklib
sudo apt-get install auditd
sudo apt-get install clamav
#sudo apt-get install $cs

#sudo auditctl -e 1						#Starts auditing
#sudo clamscan -r -i / >> clamscan.txt		#Scans for virus


echo "Changing Passwords to Student:2017 AND adding users"
input="users"
while IFS= read -r line; do
	echo "Changing password for $line"
	PASSWORD=$(openssl passwd -1 Student:2017)
	exec 2> /dev/null
	sudo adduser -disabled-password --gecos '' $line
	sudo usermod --password $PASSWORD $line
done < "$input"
exec 2>&3
echo "[DONE]"


echo "Checking for invalid users"
users=($(getent passwd {1000..60000} | cut -f1 -d':'))
for i in "${users[@]}"; do
	check=$(grep $i users)
		if [ "$check" != "$i" ]; then
			if [ "$check" != "$i" ]; then
				echo "User $i is an Unathorised user  REMOVING..."
				sudo userdel $i
			fi
		fi
		if [ "$i" != "$check" ]; then
			echo "Adding user $check"
		fi
done


echo "Chaning login.defs file"
sudo sed -i '160s/.*/PASS_MAX_DAYS	35/' /etc/login.defs
sudo sed -i '161s/.*/PASS_MIN_DAYS	15/' /etc/login.defs


echo "Disabling Guest Account"
sudo sh -c "echo allow-guest=flase >> /etc/lightdm/lightdmconf"


echo "Searching for media CHECK FILE OUTPUTS"
mkdir output
search=("mp3" "mp4" "png" "jpg" "ogg" "wav" "h264" "mpg" "mpeg" "jpeg")
for x in "${search[@]}"; do
	sudo find /home -iname *.$x > output/$x
done


echo "Setting Update Policies"
sudo sh -c "echo 'deb http://archive.canonical.com/ubuntu xenial partner' >> /etc/apt/sources.list"
sudo sh -c 'echo "deb-src http://archive.canonical.com/ubuntu xenial partner" >> /etc/apt/sources.list'
sudo sh -c 'echo "deb http://archive.ubuntu.com/ubuntu xenial main universe restricted multiverse" >> /etc/apt/sources.list'
sudo sh -c 'echo "deb-src http://archive.ubuntu.com/ubuntu xenial main universe restricted multiverse" >> /etc/apt/sources.list'
sudo sh -c 'echo "deb http://security.ubuntu.com/ubuntu/ xenial-security multiverse universe restricted main" >> /etc/apt/sources.list'
sudo sh -c 'echo "deb http://archive.ubuntu.com/ubuntu xenial-updates multiverse universe restricted main" >> /etc/apt/sources.list'



sudo ufw enable						#Turn on the firewall
sudo ufw logging on


lookfor=("nmap" "wireshark" "telnet" "ssh" "pure-ftp" "ftp" "apache" "apache2" "samba" "minetest" "ophcrack" "freeciv")
for i in "${lookfor[@]}"; do
	if [ "$i" != "$cs" ]; then
		echo; echo $i
		sudo apt-get remove $i
	else
		echo "Critical Services is $i"
	fi
done


echo "Updating..."
sudo apt-get update
sudo apt-get upgrade
