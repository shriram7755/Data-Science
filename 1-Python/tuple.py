# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:01:54 2023

@author: SHRI
"""

#tuple(access of tuple)
#tuple are used to store multiple items in a single variable

#allow dublicate
#not changable

tup1=(1,3,5,7)
print("tup1[0]:\t",tup1[0])
print("tup1[1]:\t",tup1[1])
print("tup1[2]:\t",tup1[2])
print("tup1[3]:\t",tup1[3])

#it can store different types of data
tup2=(1,'john',True,-23.45,True)
print(tup2)

#iterative over tuples
tup3=('apple','plum','orange')
for x in tup3:
    print (x)


#count how many time it occurs
tup4=('apple','plum','orange','apple','apple')
print(tup4.count('apple'))

#index of tuple
tup5=('apple','plum','orange')
print(tup5.index('plum'))

#check if element exist
tup5=('apple','plum','orange')
if 'orange' in tup5:
    print('Orange is in Tuple')
    
#Nested tuple
tup1=(1,3,5,7)
tup2=('john','denise','phoebe','adam')
tup3=(42,tup1,tup2,5.5)
print(tup3)


#update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
#x = tuple(y)

print(y)


#

#it is not possible to add or remove
#elements from a tuple;they are immutable