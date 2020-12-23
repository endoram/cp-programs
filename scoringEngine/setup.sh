echo "Setting it up..."

echo "Installing python3"

apt install python3

if [ ! -d "/bin/cyberpatriot" ]; then
	mkdir /bin/cyberpatriot
fi

FILE=/etc/systemd/system/scoringengine.service
if test -f "$FILE"; then
	echo "File Exists"
else
	#THIS FILE CREATES THE SERVICE
	cat << EOF > /etc/systemd/system/scoringengine.service

[Unit]
Description=Cyberpatriot Scoring Service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/python3 /bin/cyberpatriot/scoringengine.py

[Install]
WantedBy=multi-user.target

EOF
fi

FILE=/bin/cyberpatriot/scoringengine.py
if test -f "$FILE"; then
	echo "File Exists"
else
	cat << EOF > /bin/cyberpatriot/scoringengine.py

#THIS IS THE MAIN SCORING ENGINE
while True:
	print("WORKING!!")


EOF
fi

chmod 777 /bin/cyberpatriot/scoreingengine.py

systemctl start scoringengine	#Start the engine
systemctl enable scoringengine	#Enable it on start
systemctl daemon-reload		#Reload the daemons
#rm setup.sh			#Removes this script
