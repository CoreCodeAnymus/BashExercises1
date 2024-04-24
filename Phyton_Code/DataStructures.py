#DATA STRUCTURES

#Data plays a very important role in the current work environment. Data structures in Python enable you to store data, 
# retrieve them, and perform operations on them easily. Lists, tuples, dictionaries, and sets are four basic types 
# of data structures in Python. 

#Lists
print('---------------------------------------------------------------------------------------------------')
my_list =[] #THis how we create an empty list
print('This is the current list:',my_list)
my_list=['Potatoes',15,12,23] #We add items to the list.
print('This is the new list once we added some items:', my_list)
print('This is the current lenght of the list:', len(my_list))
print('This checks for an index', my_list.index(12))
print('This add a value to the list', my_list.append('100'))
print(my_list)
print('---------------------------------------------------------------------------------------------------')



#forLoop with lists
print('---------------------------------------------------------------------------------------------------')
for item in my_list:
    print(item)#with this code the for iteration checks and prints all items.
print('---------------------------------------------------------------------------------------------------')



#Tuples, the tuples are like the lists but they can't be changed.
print('---------------------------------------------------------------------------------------------------')
my_tuple = (1,2,'hello') #An importat difference is that we use () for tuples
print(my_tuple)
for item in my_tuple:
    print(item)
print('---------------------------------------------------------------------------------------------------')


#Dictionaries in python
print('---------------------------------------------------------------------------------------------------')
print('This is an example of a dictionary')
my_dictionary = {} #empty dictionary
print(my_dictionary)
my_dictionary = {1: 'Hello', 2: 'Bye'} #Dictionary with elements.
print(my_dictionary)
my_dictionary[3]= 'Python' #Adding a new element to dictionary
print(my_dictionary)
print('---------------------------------------------------------------------------------------------------')



#For loops with dictionary
print('---------------------------------------------------------------------------------------------------')
my_dict = {1: 'Membrillo', 2: 'Pepegrillo'}
for key, value  in my_dict.items():
    print (key , '->', value)
for value in  my_dict.values():
        print('value:', value)
for key in  my_dict.keys():
        print ('key:', key)
print('-------------------------------- -------------------------------------------------------------------')



#SETS
#Sets are a collection of unordered elements that are unique. They only hold unique values and duplicate 
#values are automatically deleted in the set.
#Sets are created by placing comma-separated values inside parentheses {}
print('---------------------------------------------------------------------------------------------------')
my_set = {1,2,2,2,5,5,5,5,5} #We create a set.
print(my_set)
for item in my_set:
      print(item)
print('---------------------------------------------------------------------------------------------------')


#Functions
print('---------------------------------------------------------------------------------------------------')
def addition (num1, num2): #it is created the function addition.
      result = num1 + num2 #we assign the result of the sum to result variable
      return result #we indicate the terminal to return the value result
print(addition(1,100)) #we print the function addition with two parameters.
print('---------------------------------------------------------------------------------------------------')


#Import Module
print('---------------------------------------------------------------------------------------------------')
import math #Imports math library
print(math.pow(9,3)) #returns the value of 9 raised to the power of 3
print(math.acos(0.55)) #returns the arc sen of 0.55
print('---------------------------------------------------------------------------------------------------')



