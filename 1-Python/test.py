# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:58:42 2023

@author: SHRI
"""

#write a python function that takes two list and true if they have at least one common element member
lst1=[1,4,5,6,7]
lst2=[4,6,8,9,10]
def my_func(lst1,lst2):
    a=[a for a in lst1 if a in lst2]
    print(a)
    if len(a)>=1 :
        print("True")
    
my_func(lst1, lst2)



#using list comprehension to construct a new list but add 6 to each item
old_lst=[1,2,3,4,5,6]
lst=[a+6 for a in old_lst ]
print(lst)




'''
def my_c(old_lst):
    yield lambda x:x+6
lst=[a for a in my_c(old_lst)]
print(lst)
'''

#write a python program to reverse the string
s='shrirambuchkul'
a=s[::-1]
print(a)

#Write a Python program to iterate over the dictionary using for loop

dict={
      'A':30,
      'B':40,
      'C':70,
      'D':90
      }

for i in dict:
    print(i , end=':')
    print(dict[i])
    
    
#





#6 file handling

with open('data.txt') as file:
    c=file.read()
    
print(c)

with open('pi_digits.txt') as file:
    c=file.read()
    
print(c)
with open('shri.txt') as file:
    c=file.read()
    
print(c)
    






#8write a python program to construct an



# filter list of integer using lambda function

lst1=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
ev=lambda x:x%2==0
for x in lst1:
    if ev(x):
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)
      
        
#9 write a pandas program to create 



#9
import pandas as pd
import numpy as np
dict={
      'name':['anna','dinu','ramu','ganu','emily','mahesh','jayesh','venkat','ajay','dhanesh'],
      'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
      'attempts':[1,3,2,3,2,3,1,1,2,1],
      'qualify':['yes','no','yes','no','yes','yes','no','no','yes','no'],
      }
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(dict,index=labels)
df




#10
import matplotlib.pyplot as plt
plt.plot([2,6,3,6,3])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show 


















