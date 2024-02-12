#!/bin/bash
#This is an another example of how the if command works on bash

echo "Enter a number you wish"
read n
if [ $n -lt 10]
then 
echo "It is a one digit number"
else
echo "It is a two digit number"
fi
