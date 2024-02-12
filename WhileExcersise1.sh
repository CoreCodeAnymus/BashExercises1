#!/bin/bash

#This is an example of while loop
#Equal to ==
#Not equal to !=
#Grater than >
#Less than <

echo "Type a number to know if you know the password"
read pass

while [ $pass != 8 ]
do 
 echo "Wrong number, guess again"
 read pass
done
