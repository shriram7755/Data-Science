o# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:20:09 2023

@author: SHRI
"""
###################################  List Comprehension ###################################


################################
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#############################
#list comprehension
#we can write same method using list comprehension

lst=[num for num in range(0,20)]
print(lst)

############################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)

names=['dada','mama','kaka']
lst=[name.title() for name in names]
print(lst)

##############################
#list comprehension with if 
#if statement on right side executed first then for statement on left side executed

def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

##
def is_odd(num):
    return num%2!=0
lst=[num for num in range(10) if is_odd(num)]
print(lst)

##
lst=[f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)

######################## set Comprehension ###########################

set_one={x for x in range(3)}
print(set_one)


################## Dictionary Comprehension ################

dict={x:x*x for x in range(3)}
print(dict)


#Genetators 
# It is another way of creating iterators
# in a simple where
#it usages the keyword "yield"
#insted of returing  it is defined function
#gen -object
# when  we  are using tuple comprehension , one object will be created 
#we can access the values using for loop
# tuple  are creating object in tuple comprehension
#while list, dict, set are not creating object.

gen=(x for x in range(3))
print(gen)

for num in gen:
    print(num)
    
#another method
#next method showing output step by step
gen=(x for x in range(3))

next(gen)
next(gen)
next(gen)

###########
#Function which return multiple value

def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
#now insted of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
next(gen)

##########
#chaining of Generators
def lengths(itr):
     for ele in itr:
         yield len(ele)
         # to measure the length of password
         
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
passwords=["not-good","give'm-pass","00100=100"]

for password in hide(lengths(passwords)):
    print(password)

##### Enumerate : display result in terms of key: value
#printing list with index

lst=['milk', 'Egg','Bread']
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
####################

lst=['milk', 'Egg','Bread']
for index,item in enumerate(lst ,start=1):
    print(f"{index} {item}")



import string
#Pick adjectives
adjectives = ['sleepy','slow','smelly','wet','fat','red','yellow','blue','black','white','proud','brave']
#Pick noun
nouns = ['apple','dinosaur','ball','goat','cow','baffalo','duck','hen']
#Pick the words
import random

adjective = random.choice(adjectives)
noun = random.choice(nouns)
#Select a number
number = random.randrange(0, 100)
#Select a special character
special_char = random.choice(string.punctuation)
#Create the new secure password
passwords = adjective + noun + str(number) + special_char
#print('Your new password is : %s' %password)


def lengths(itr):
     for ele in itr:
         yield len(ele)
         # to measure the length of password
         
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
#passwords=["not-good","give'm-pass","00100=100"]

for password in hide(lengths(passwords)):
    print(password)



###############################################################
#IMP interview
#zip function
#NLP operation 
#Web Screapping

name = ['data','mama','kaka']
info=[9850 , 6032,9785]

for nm,inf in zip(name,info):
    print(nm,inf)

#mismatch list

name = ['data','mama','kaka','baba']
info=[9850 , 6032,9785]

for nm,inf in zip(name,info):
    print(nm,inf)
#It will not display excess mismatch items in name
#i.e 'baba'

######################
# zip_longest
from itertools import zip_longest
name = ['data','mama','kaka','baba']
info=[9850 , 6032,9785]

for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
##################################
#feature engineering use 
# use of fill value insted None
#for machine learning op
from itertools import zip_longest
name = ['data','mama','kaka','baba']
info=[9850 , 6032,9785]

for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
#########################
#use of all() if all the values are true it will produce output.
#all - +ve and -ve value 
lst=[2,3,-6,8,9] # value must non-zero positive and negative


if all(lst):
    print("all values are true ")
else:
    print("useless")
    
#################################
##########################

lst=[2,3,0,8,9]
if all(lst):
    print("all values are true ")
else:
    print("useless")   #  zero value return
    
    
# use of 'any' if any one non zero value
#any- non zero value in list 
lst=[0,0,0,8,0]
if any(lst):
    print('it has some value')
else:
    print('useless')
    
#use of any
lst=[0,0,0,0,0]
if any(lst):
    print('it has some value')
else:
    print('useless')


#cout - application iot
#count()
#used in Ai

from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

# now let us start from 1

from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#cycle()
#suppose you have repeated task to be done, the you can use this method

import itertools

instructions=("Eat",'code',"sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
    
#repeat()
from itertools import repeat
for smg in repeat("keep patience",times=3):
    print(smg)
    
#permutation: relates to the act of arranging all the 
#members of a set into some sequence or order

#The combination is a way of selecting items from a 
#collection, such that (unlike permutations) the order 
#of selection does not matter.

# Combination
#

from itertools import combinations
players=['rahul','manisha', 'gayatri']
for i in combinations(players, 2):
    print(i)
    
    
#permutation
from itertools import permutations
players=['rahul','manisha', 'gayatri']
for seat in permutations(players, 2):
    print(seat)
    
#product
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['virat','Manish','Sami']

for pair in product(team_a,team_b):
    print(pair)
    
    
###################
#filter function

age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)  # lamda function
print([age for age in adults])   #list comprehension

##############################
#IMP in interview
#shallow copy and deep copy

#assignment operation
#what even the change are there in list_a[0] will also reflected in list_b
#this will create a new variable
 
list_a=[1,2,3,4,5]
list_b=list_a
list_b[0]=-10
print(list_a)
print(list_b)

#shallow copy
#its create a seperate instances
#one level deep . modifing on level 1 does not affect the other list
#shallow copy : create a data object one level deep copy
#modifying  level one  does affect the other list
#in order to create the shallow copy "copy function of copy module " is used
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#not affect the other list
list_b[0]=-10
print(list_a)
print(list_b)

#But with nested object

list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affect the other !
#with two level its affect the other list.
#i.e list_a=[[1,2,3,4,5],[6,7,8,9,10]]

list_a[0][0]=-10
print(list_a)
print(list_b)

############################################
#deep copy
#Full independent clone  .use copy.deepcopy()

import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#not affect the other 
list_a[0][0]=-10
print(list_a)
print(list_b)





#################### itertool Assignment ###########################
#write a python program to create an iterator from several iterable 
#in a sequence and display type and element of the new iterator.



# chain operator
#use nlp ,ml model
from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)

#list
result=chain_func([1,2,3], ['a','b','c','d'], [4,5,6,7,8,9])
print("type of the new itearor :")
print(type(result))
print("Element of the new iterator")
for i in result:
    print(i)
    
    
#Tuple

result=chain_func((1,2,3), ('a','b','c','d'), (4,5,6,7,8,9))
print("type of the new itearor :")
print(type(result))
print("Element of the new iterator")
for i in result:
    print(i)
    
    
#write a python program that generates the running product
#of element in an iterable.

from itertools import accumulate
import operator   # do all mathe,atical opeartion
def running_product(lst):
    return accumulate(lst,operator.mul)  # mul for multiplication

#list
lst=running_product([1,2,3,4,5,6,7])
print("Running Product of list: ")
for i in lst:
    print(i)
    
#write python program to construct an infinite iterator that
#return evenly spaced values starting with a specified number and step.
# 


import itertools as it

start=10
step=1
print("starting point is ",start ,"and step is ",step)
my_counter=it.count(start,step)
#following loop run for ever
print("The said function print never-ending items: ")
for i in my_counter:
    print(i)
    
    
#############################
#write python program to generate an infinite cycle 
#of element from an iterable.

import itertools as it 
def cycle_data():
    return it.cycle(iter)

#following loop run for ever
#list

result=cycle_data(['Aiter','B','C','D'])
print("THe said function print never-ending items: ")
for i in result:
    print(i) 
    
# for string 
result =cycle_data('Python itertools')
print("THe said function print never-ending items: ")
for i in result:
    print(i)



# write a python program to make an iterator that drops
#elements from the iterable as soon as element is positive number


import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0 , nums)

nums=[-1.-2,-3,4,-10,2,0,5,12]

print("Original list: ", nums)
result=drop_while(nums)

print("Drop element from the iterable when positive number arises \n",list(result))
