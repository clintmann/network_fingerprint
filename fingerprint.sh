#!/usr/bin/env bash

echo
echo "################################################"
echo "Thank you for using the Network Fingerprint App "
echo "--"
echo "This script will set up the environment to"
echo "monitor the Spark Room."
echo "--"
echo "It will also setup the application that makes"
echo "API calls to your Cisco Identity Services Engine"
echo
echo "################################################"
echo


echo "Press Enter to continue..."
read confirm

echo "Please enter YOUR Spark AUTHENTICATION TOKEN : "
read -s TOKEN

echo "Please enter the Spark AUTHENTICATION TOKEN of the BOT : "
read -s BOTTOKEN

echo "Please enter the Spark ROOM ID : "
read -s ROOMID

echo "Next we will set up AUTHENICATION for ISE"
echo "-----------------------------------------"
echo "Press Enter to continue..."
read confirm

echo "Please enter the IP ADDRESS of the ISE SERVER : "
read -s ISEIPADDR

echo "Please enter ISE USERNAME (must have MnT Admin rights) : "
read  ISEUSER

echo "Please enter the PASSWORD for the USER entered above : "
read -s ISEUSERPWD


python ./app/fingerprint-app/monitorspark.py $TOKEN,$BOTTOKEN,$ROOMID
python ./app/fingerprint-app/ise_search.py $ISEIPADDR $ISEUSER $ISEUSERPWD
