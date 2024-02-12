#!/bin/bash 

#This is an small networking script.

clear
user=`whoami`
day=`date`
ip=`hostname -i`
hname=`hostname`

if [ $user = 'root' ]
then
figlet "Network"
echo "The date is: $day)"
echo "The user is: $user"
echo "The ip is: $ip"
echo "The hostname is: $hname"
echo "$(netstat -antp)"
else 
   echo "You're not allowed to run this command..."
fi
