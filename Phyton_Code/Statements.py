# Write your code here :-)
print('This is the first hello world:')
print('Hello word')
print('---------------------------------------------------------------------------------------------------')
#This is a comments
#Here it will start different set of code lines

#Aritmetic
print('---------------------------------------------------------------------------------------------------')
print('This is where the Aritmetic examples begin:')
print(2+2) #Sum
print(2-2) #Substraction
print(2*2) #Multiplication
print(2/2) #Division
print(2%2)  #Module
print('---------------------------------------------------------------------------------------------------')

#Logic operators\
print('---------------------------------------------------------------------------------------------------')
print('These are logical operators:')
print ( True and True)
print (True or False)
print('---------------------------------------------------------------------------------------------------')

#Statements

#If Statement
print('---------------------------------------------------------------------------------------------------')
print('If Statment example')
i=1000
if (i>100):
    print ( f'{i} is greather than 100')
print('---------------------------------------------------------------------------------------------------')


#If else statement
print('---------------------------------------------------------------------------------------------------')
print('If else statement')
l=10
if (l>100):
    print(f'{l} is greater than 100')
else:
    print (f'{l} is less than 100')
print('---------------------------------------------------------------------------------------------------')


#Elif statement
print('---------------------------------------------------------------------------------------------------')
k=10
if (k > 100):
    print(f'{k} is greater than 100')
elif(k>1):
        print(f'{k} is greater than 1')
elif(k==10):
    print(f'{k}is equal to 10')
else:
    print(f'{k} is less than 1')
print('---------------------------------------------------------------------------------------------------')

#FOR Loops
print('---------------------------------------------------------------------------------------------------')
for x in range(4):
    print(x)
print('---------------------------------------------------------------------------------------------------')


#While Loop
print('---------------------------------------------------------------------------------------------------')
print('This is how a loop works on python')
m = 1
while m < 4:
    print (m)
    m +=1
print('---------------------------------------------------------------------------------------------------')


#Break example
print('---------------------------------------------------------------------------------------------------')
for x in range(4):
    if x == 2:
        break
    print(x)
print('---------------------------------------------------------------------------------------------------')


#Continue example
print('---------------------------------------------------------------------------------------------------')
for x in range(4):
    if x == 2:
        continue
    print(x)
print('---------------------------------------------------------------------------------------------------')



















