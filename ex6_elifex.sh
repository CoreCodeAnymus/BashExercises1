#!/bin/bash

#This an example using else if with bash

echo "Enter your lucky number"
read n
 if [ $n -eq 101];
then 
echo "You've got the first prize"
elif [$n -eq 522];
then 
echo "You've got the second prize"
elif [$n -eq 999];
then
echo "You've got the third prize"
else
echo "Sorry, try for the next time."
fi

