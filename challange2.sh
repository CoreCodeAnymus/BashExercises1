#!/bin/bash

#Challange2 using functions


#Functions
message1 (){
echo "Please enter the admin user:"
}

message2 (){
echo "Please enter the  user password:"
}

noaccess (){
echo "You don't have access with this user..."
}

noaccess1 (){
echo "Password incorrect"
}


#Variables
useradmin="june"
pass="tristan"

#-Message1--------------------------------------------------
message1
read an1

if [ $an1 != $useradmin ]
then
echo  "-----------------------------------------------"
noaccess
else
#Message2-------------------------------------------------
message2
read an2

if [ $an2 != $pass ]
then
echo  "-----------------------------------------------"
noaccess1
else
 echo "Welcome $(whoami)"
fi
fi








