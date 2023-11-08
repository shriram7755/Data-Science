# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:33 2023

@author: SHRI
"""

#Exception are handled with try-except blocks.


print(5/0)

#Using try-except Block

a=5
b=6
c=a=b
#print(5/0)


try:
    print(5/0) #get file

except TypeError :
    print("You can't Divide by Zero!")
except ArithmeticError:
    print("You can't Divide by Zero! 22222")

except ZeroDivisionError:
    print("You can't Divide by Zero! 11111") # Dead block of code bad coding.


print("After Division")
    
    
print(c)




#Handling the fileNotFound Exception
#Today’s programs need to be able to handle a wide variety of characters.
# Applications are often internationalized to display messages and output in a
# variety of user-selectable languages; the same program might need to output
# an error message in English, French, Japanese, Hebrew, or Russian. 
#Web content can be written in any of these languages and can also include a 
#variety of emoji symbols. Python’s string type uses the Unicode Standard
# for representing characters, which lets Python programs work with all these
# different possible characters.

# UTF - Unicode transformation Format.
#UTF-8 has several convenient properties:

#It can handle any Unicode code point.

############################################
#write on quick reference pages and highlights


filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
    
##############################################
"""
Many of your progrsms will ask user to input 
certain kinds of information.
You might allows user to store preferences 
in a game or provide in data structures 
such as lists and dictionaries.
When user close a program,
you shall almost always want to save 
the information they entered.
A simple way to do this involves 
storing the data using json module.
"""
"""the JSON (JavaScript Object Notation) format was 
originally developed for Java using json.dump()
and json.load()
"""

#  The JSON (JavaScript Object Notation ) format was originally Developed by JAVA
#using json.dump() and json.load()


import json

numbers= [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename, 'w') as f :
    json.dump(numbers,f)
    

################
#saving data with json is useful
#when you are working with user generated data

import json

username=input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f :
    json.dump(username,f)
print(f"We'll remember you when you come back , {username}!")
    
    
# Now let's write a new program that greets
# a user whose name has already been stored

import json


filename = 'username.json'
with open(filename, 'w') as f :
    #username =json.load(f)
    json.dump(username,f)
print(f"Welcome back , {username}!")  


############################################
#load the username , if it has been store previously.
#otherwise, prompt for the username and store it



filename ='username.json'
  
#write a python script to add a key to a dictionary.
#sample Dicctionary : {0,10,1:20}
#Expected Result : {0:10 ,1:20,2:30}
    
d= {0:10,1:20}
print(d)
d.update({2:30})
print(d)

####################

d={0:10, 1:20}
print(d)
d[2]=30
print(d)
    
    
# write a python script to concatenate the following
#dictionary to create a new code.
#Sample Dictionary :
dic1={1:10 ,2:20}
dic2={3:30 ,4:40}
dic3={5:50 ,6:60}

dict4= {}

for d in (dic1,dic2,dic3):dict4.update(d)
print(dict4)    


 
    
#write a Python Script to check wheather a given 
#key already exist in dictionary

d={1:10,2:20,3:30,4:40,5:50,6:60}

def is_key_present(x):
    if x in d:
        print("key is present is dictionary")
    else:
        print("key is not present is dictionary")
is_key_present(5)
is_key_present(9)

#------------------------------------------------------------------------------
#write a python program to iterate over dictionary.
#using for loop

d={'x':10,'y':20,'z':30}

for dict_key, dict_value in d.items():
    print("dict_key",':',dict_value)
    
#------------------------------------------------------------------------------
    
    
    
    
    
    
    