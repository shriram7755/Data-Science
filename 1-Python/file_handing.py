# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:45:07 2023

@author: SHRI
"""
#file handling in python
with open('pi_digits.txt')  as file_object:     #'pi_digits.txt' -relative path
    #The open function needs 
    #one arguments: the name of the file you want to open
    contents = file_object.read()
print(contents)
print(contents.rstrip())  # to remove  white space , to strips
#character from right


#two types of path  
#1)relative path
#2)absoulate path  in windows os follws \ \ follows back slash path
# working on  mac environment  gives  / / path.
#absoulate path ex : windows\system32\file_name.txt
 
file_path='c:/1-python/pi_digits.txt'
with open(file_path)  as file_object:
    #The open function needs 
    #one arguments: the name of the file you want to open
    contents = file_object.read()
print(contents)
print(contents.rstrip())


#Reading line by line 
filename ='pi_digits.txt'
#assign the name of the file we're reading from the variable
with open(filename) as file_objects:
    #we again use the with syntex to
    #let Python open and close 
    #the file properly

    
    for line in file_objects:
        print(line)
        
#Remove white space
#rstrip()       
filename ='pi_digits.txt'
#assign the name of the file we're reading from the variable
with open(filename) as file_objects:
    #we again use the with syntex to
    #let Python open and close 
    #the file properly
    
    
    for line in file_objects:
        print(line.rstrip())
        
#Working with file contents 
#after you read file in memory
#you can do  whatever you want with that data


filename ='pi_digits.txt'
with open (filename) as file_object:
    lines =file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string+=line.rstrip()
        print(pi_string)
        print(len(pi_string))


##Writing to a file.

filename= 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I Love Programming")
    
#writing multiple files 
# the write function does not add new line
# to the text you write. so if
#you write more than one line without 
#including newline character

filename= 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I Love Programming")
    file_object.write("\nI Love Creating new Games")
    
    
#for new line

filename= 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I Love Programming.\n")
    file_object.write("I Love Creating new Games.\n")
    
    
#appending a file
#you can open file in append mode
#Python does not erase the content of file
#Before returning the file object
filename= 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I Love Programming.\n")
    file_object.write("I Love Creating new Games.\n")
    
