# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:05:15 2023

@author: SHRI
"""

###########################################################################################

#set
#duplicates not allows in set

#creating set

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#when run this code will show that the apple is only added once to the list

#accessing Element in list

for items in basket:
    print(items)

#Adding item to set

basket ={'apple ' ,'banana', 'cheery'}
basket.add('apricot')
print(basket)

g
#IF you want to add more items to a set the we can use list
basket ={'apple ' ,'banana', 'cheery'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)

#obtaining the length of a set
basket={'banana', 'grapefruit', 'cheery', 'apple ', 'mango', 'apricot'}
print(len(basket))


#max and min
basket={23, 45,67,12,456}
print(max(basket))
print(min(basket))


#Removing an Items
basket={'banana', 'grapefruit', 'cheery', 'apple', 'mango', 'apricot'}
print(basket)
basket.remove('apple')
basket.discard(('apricot'))
print(basket)


#set operation

s1={'apple','banana', 'orange'}
s2={'grapefruit','line','banana'}
print("Union: ",s1|s2)
print("Intersection: ",s1&s2)
print("Difference: ",s1-s2)