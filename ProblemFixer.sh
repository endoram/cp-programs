#!/bin/bash

clear
echo "********************************"
<<<<<<< Updated upstream
echo "*   Problem Fixer Version 1.0  *"
=======
echo "*     Bee-Secure Version 1.0   *"
>>>>>>> Stashed changes
echo "*   Made By Spencer McConnell  *"
echo "********************************"

echo

cd /etc

echo "********************************"
echo "*   Changing PASS_MASS_DAYS    *"
echo "********************************"

sudo sed -i '160s/.*/PASS_MAX_DAYS	35/' login.defs
read pasw

echo
echo pasw
echo

sleep 2
echo "[Done]"
echo

echo "********************************"
echo "*    Changing PASS_Min_DAYS    *"
echo "********************************"

sudo sed -i '161s/.*/PASS_MIN_DAYS	15/' login.defs
sleep 2
echo "[Done]"

#cd /etc/pam.d

sleep 5

#echo "********************************"
#echo "*   Changing common-password   *"
#echo "********************************"

echo "Searching home"
echo
ls /home
echo
echo "********************************"

sleep 3

echo "Searching Desktop"
echo
ls /home/"$USER"/Desktop
echo
echo "********************************"

sleep 3

#Define some vars

no=n
yes=y

echo
echo  "$version_number"
echo

################################################################
#                    Searching Downloads                       #
################################################################

echo "Searching Downloads"
ls /home/"$USER"/Downloads
echo
echo "Do you want to Delete everything in Downloads?[y/n]"
read answer0

if [ "$answer0" == "$no" ]
then
	echo "ok moving on..."
	echo "********************************"
else
	echo "now removing everything in Downloads"
    cd /home/$USER/Downloads
    #sudo rm *
    ls
	echo "[Done]"
	echo "********************************"
fi

################################################################
#                     Searching Documents                      #
################################################################

echo "Searching Documents"
ls /home/"$USER"/Documents
echo
echo "Do you want to Delete everything in Douments?[y/n]"
read answer0

if [ "$answer0" == "$no" ]
then
	echo "ok moving on..."
	echo "********************************"
else
	echo "now removing everything in Documents"
    cd /home/$USER/Documents
    #sudo rm *
    ls
	echo "[Done]"
	echo "********************************"
fi

################################################################
#                       Searching Videos                       #
################################################################

echo "Searching Videos"
ls /home/"$USER"/Videos
echo
echo "Do you want to Delete everything in Videos?[y/n]"
read answer0

if [ "$answer0" == "$no" ]
then
	echo "ok moving on..."
	echo "********************************"
else
	echo "now removing everything in Videos"
    cd /home/$USER/Videos
    #sudo rm *
    ls
	echo "[Done]"
	echo "********************************"
fi


################################################################
#                       Searching Music                        #
################################################################

echo "Searching Music"
ls /home/"$USER"/Videos
echo
echo "Do you want to Delete everything in Music?[y/n]"
read answer0

if [ "$answer0" == "$no" ]
then
	echo "ok moving on..."
	echo "********************************"
else
	echo "now removing everything in Music"
    cd /home/$USER/Music
    #sudo rm *
    ls
	echo "[Done]"
	echo "********************************"
fi


################################################################
#                     Searching Pictures                       #
################################################################

echo "Searching Pictures"
ls /home/"$USER"/Videos
echo
echo "Do you want to Delete everything in Prictures?[y/n]"
read answer0

if [ "$answer0" == "$no" ]
then
	echo "ok moving on..."
	echo "********************************"
else
	echo "now removing everything in Pictures"
    cd /home/$USER/Pictures
    #sudo rm *
    ls
	echo "[Done]"
	echo "********************************"
fi


################################################################
#                     Searching Trahs                          #
################################################################

echo "Searching Trash"
ls /home/"$USER"/Trash
echo
echo "Do you want to Delete everything in Trash[y/n]"
read answer0

if [ "$answer0" == "$no" ]
then
	echo "ok moving on..."
	echo "********************************"
else
	echo "now removing everything in Trash"
    cd /home/$USER/Trash
    #sudo rm *
    ls
	echo "[Done]"
	echo "********************************"
fi

echo
echo
echo
echo

##################################################
#             Disabling Guest Account            #
##################################################

echo "      ##################################################
      #             Disabling Guest Account            #
      ##################################################"

sudo /usr/lib/lightdm/lightdm-set-defaults -l false
echo "[Done]"



if

unity-control-center
