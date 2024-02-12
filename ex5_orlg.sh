#!/bin/bash

#This is a little game that will show how to use the OR logic gate.
# The signs "||" will represent the or logic gate at this language, let's start.

printf "\n"
echo "-------------------------------------------------"
echo "Let's play a game,
I have in mind two numbers. 
You have two opportunities to guess at least one of them.
A clue: The range of the numbers I have in mind is 1 to 25 "
echo "-------------------------------------------------"

printf "\n"
echo "Enter any number you wish"
read n1
echo "Enter any other number you wish"
read n2

if [[( $n1 -eq 8 || $n2 -eq 22)]]
then
echo "Congratulations you have guessed a number!"
else
echo "Nope, none of the numbers are the numbers I thougth."
fi

