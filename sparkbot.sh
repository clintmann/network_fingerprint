#!/usr/bin/env bash


echo
echo "###############################################"
echo "Thank you for using the Network Fingerprint App"
echo  "This script will set up the environment to "
echo  "configure the Fingerprint Sparkbot"
echo "###############################################"
echo

echo "Press Enter to continue..."
read confirm

echo "Please enter the NAME of the Bot : "
read BOTNAME

echo "Please enter the EMAIL ADDRESS of the Bot : "
read BOTEMAIL

echo "Please enter the AUTH TOKEN for the Bot : "
read -s BOTTOKEN

# pip install required python libraries
#sudo -E pip install --upgrade pip
# following needed when upgrading pip in Amazon Linux
#sudo -E cp /usr/local/bin/pip /usr/sbin/

# create a folder to store scripts in
#sudo mkdir scripts/

wget "https://raw.githubusercontent.com/clintmann/network_fingerprint/master/fingerprintBOT.py"


sed -i "s/<BOTNAME>/$BOTNAME/" fingerprintBOT.py
sed -i "s/<BOTEMAIL>/$BOTEMAIL/" fingerprintBOT.py
sed -i "s/<BOTTOKEN>/$BOTTOKEN/" fingerprintBOT.py


#nohup python fingerprintBOT.py &