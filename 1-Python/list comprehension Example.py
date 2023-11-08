
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:14:46 2023

@author: SHRI
"""

###################################### list Comprehension ################################
syntex = [  for                        if                  ]
#if else exist the syntex changes 
syntax = [ if                  else                      for          ]






#find all of the numbers from 1-1000 that are divisible by 7
div7 =[n for n in range(1,1000) if n%7==0]
print(div7)





#Find all the numbers from 1-1000 that have 3 in them
three=[n for n in range(1,1000) if '3' in str(n)]
print(three)



#Count the no of spaces in the string
some_string='the slow solid swam sumptuously three through the slimy swamp'

spaces=[s for s in some_string if s==' ']
print(len(spaces))



#creating a list of all consonents in the string 
#Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams

sentence= '''Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams'''

result = [letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(result)



#find common no in two list without using a tuple or set.

list_a = [1,2,3,4]
list_b =[2,3,4,5]

common = [a for a in list_a if a in list_b]
print(common) 




#IMP
##web scrapping
# Get only the numbers in a sentence like 'In 1984 there were 13 instances of a
#  The isalpha() method returns True if all the characters are alphabet letters (a-z) 

sentence= 'In 1984 there are 13 instances of a  protest  with over 1000 people attending'
words =sentence.split()
words
result=[number for number in words if not number.isalpha()]
print(result)



"""
Given numbers = range(20), produce a list 
containing even and odds
"""

result = []
for n in range (20):
    if n%2==0:
        result.append('even')
    else:
        result.append('odd')
print(result)

##List comprehension
[result =[f'{n} :even' if n%2==0 else f'{n}:odd' for n in range(20)]
print(result)]




'''produce a list of tuples consisting of only 
the matching numbers in these lists list_a=[1,2,3,4,5,6,7,8,9],
list_b=[2,7,1,12].'''

list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a==b]
print(result)




#####################################
#  find all of the words in a string that are less than 4 letters

sentence = 'On a summer day Ramnath sonar went swimming in the sun and his red skin stung'

examine=sentence.split()

result = [word for word in examine if len(word)<=4]
print(result)



# write python program to print a specified list
#after removing the oth , 4th , and 5th elements,
#enumerate i.e key:value

colour = ['Red', 'Green', 'White','Black','Pink','yellow']

colour = [x for (i,x) in enumerate(colour) if i not in(0,4,5)]
print(colour)




#######################################
#write a python program that create a generator function 
#that yields cubes of numbers from  1 to n . accept n from user

def cube_generator(n):
    for  i in range(1,n+1):
        yield i**3
#accept input from user 
n=int(input("Enter no: "))
#Create a Generator object 
cubes =cube_generator(n)

#iterator over generator and print the value
print("Cubes of numbers from 1 to",n)
for num in cubes:
    print(num) 
    
###################################################    
# Write python program to implement a generator that generatates
#a random number within a given range

import random
def random_number_generator(start,end):
    while True:
        yield random.randint(start, end)
        
#accept input from user

start=int(input("Enter start no: "))
end=int(input("Enter end no : "))

##Create a Generator object 

random_number=random_number_generator(start,end)

#iterator over generator and print the value
print("Print random No between",start, "End ", end)
for _ in range(10):
    print(next(random_number))
    
    


###################################################################
#if [[    ]] there are 2 square brack there is 2 D arrray
#if [[  [          ]   ]] there are 3 square brack there s 3 D arrray

#write a Python program to generate a 3*4*6 3D array whose each element 
array = [[[ '*' for col in range(6)] for col  in range(4)] for row in range(3)]
print(array)

#write a python programm to print a number of 
#specified list after removing even number from it.

num=[7 ,8, 120, 25, 44, 20, 27]
num=[x for x in num if x%2!=0]
print(num)

#write a python programm to print a number of 
#specified list after removing odd number from it 

num=[7 ,8, 120, 25, 44, 20, 27]
num=[x for x in num if x%2==0]
print(num)

Home Work 
#compare two sentences and find out common word in that sentences

def sentence_to_list(sentence1):
    word=sentence1.split()
    return word

sentence1 ="This is very big news related with data science field"

list_a=sentence_to_list(sentence1)
#print(list_a)


def sentence_to_list(sentence2):
    word=sentence2.split()
    return word

sentence2 ="Our Aim is to Find out data science field"

list_b=sentence_to_list(sentence2)
#print(list_b)


common = [a for a in list_a if a in list_b]
print(common) 

#find out common word in that sentences


def sentence_to_list(sentence1):
    word=sentence1.split()
    return word

sentence1 ="This is very big news is related with data science field"

list_a=sentence_to_list(sentence1)
#print(list_a)

common = [a for a in list_a for b in list_a if a==b]
print(common)


 
