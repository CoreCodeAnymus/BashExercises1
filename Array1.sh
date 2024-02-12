#!/bin/bash

#Arrays


g=('Milk' 'Chocolate' 'Popcorns' 'Fruits' 'Eggs' 'Vegetables' 'Soda' 'Water')


echo "------------------------------------------------------"
echo "This is the first item at the groceries array ${g[0]}"
echo "This is the second item at the groceries array ${g[1]}"
echo "This is the third item at the groceries array ${g[2]}"
echo "This is the fourth item at the groceries array ${g[3]}"
echo "This is the fifht item at the groceries array ${g[4]}"
echo "This is the sixth item at the groceries array ${g[5]}"
echo "This is the seventh item at the groceries array ${g[6]}"
echo "This is the eight item at the groceries array ${g[7]}"
echo "These are all the items at the groceries array:"
echo ${g[@]}

#To delete an item
unset g[3]
echo "Let's delete the fourth element @Fruits from the array"

#To modify an item
echo "------------------------------------------------------"
g[5]='Butter'
echo "Let's modify the fifht element @Eggs at the array"
echo "Now this is the updated list:   ${g[@]}"
echo "------------------------------------------------------"
