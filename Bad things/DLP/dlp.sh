#!/bin/bash

#Check if python script is running (shutit.py)
if pgrep -f "python3 shutit.py" &>/dev/null; then
	echo "Script is running"
	FILE = /home/spencer/showkey/swapit
	if test -f "$FILE"; then
		rm /etc/fstab
		#SCP has been operated
		cat << EOF > /etc/fstab
		# /etc/fstab: static file system information.
		#
		# Use 'blkid' to print the universally unique identifier for a
		# device; this may be used with UUID= as a more robust way to name devices
		# that works even if disks are added and removed. See fstab(5).
		#
		# <file system> <mount point>   <type>  <options>       <dump>  <pass>
		# / was on /dev/sda2 during installation
		UUID=a8befabf-1ef0-40c8-a126-1f599fa43ec9 /               ext4    errors=remount-ro 0       1
		# /boot/efi was on /dev/sda1 during installation
		UUID=802E-46E9  /boot/efi       vfat    umask=0077      0       1
		# /home was on /dev/sda3 during installation
		UUID=THIS IS WHERE YOU PUT THE ALT. PARTION ID /home           ext4    defaults        0       2
		/swapfile                                 none            swap    sw              0       0
		EOF
		
		sdd="/dev/sda"
		for i in $sdd; do
			echo "
			d
			5
			w
			" | fdisk $i; done
		reboot
	fi

else
	WEBHOOK=PUT YOUR WEBHOOK HERE
	MESSAGE="ERROR - System Protection Service Not Opperational"
	echo $MESSAGE
	./home/spencer/showkey/discord.sh --webhook-url=$WEBHOOK --text="$(echo $MESSAGE)"
	sleep 300
fi
