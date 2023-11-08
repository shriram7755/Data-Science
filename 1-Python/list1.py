# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:02:33 2023

@author: SHRI
"""

########################################################################

#LIST

#creating list
#allow dublicate
#changable

list1=[1,14.3,True]

#nested list
list1=[1,14.3,True]
list2=['apple','orange',31]
root_list=['john',list1,list2,'denise']
print(root_list)

#accessing through index
list1=['john','paul','george','ringo']
print(list1[-1])
print(list1[0])
print(list1[-2])
print(list1[1:3])
print(list1[:3])
print(list1[1:])

#adding to list
list1=['john','paul','george','ringo']
list1.append('pete')
print(list1)

#extend a list
#extend a list
lst1=['om','paul','krushna','ringo','pete']
lst1.extend(['Shri','tomy'])
print(lst1)




#insert to list

a_list=['tomy','madonna','om']
print(a_list)
a_list.insert(1,"shri")
print(a_list)





#list concatenation
lst1=[3,2,1]
lst2=[6,5,4]
lst3=lst1+lst2
print(lst3)


#Remove from the list
another_list=['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_list)
another_list.remove('Robbie')
print(another_list)


#The pop() method 
another_list=['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
another_list=['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_list)
another_list.pop(2)
print(another_list)

#Insert Element in a list

a_list=['apple' ,'banana', 'cheery']
print(a_list)
a_list.insert(3,'Paloma')
print(a_list)
   
##############################3    
#Home work
#find out max element in a list
list=[1,5,7,13,25,36,19]
x=max(list)
print(x)

#HW take 5 string in list and make it reverse
list=[]
n=int(input("Enter list size:  "))
for i in range(0,n):
    a=input("Enter string: ")
    list.append(a)
print(list)
list.reverse()
print(list)   

#HW take 10 no in list write script to search value
list=[]
n=int(input("Enter list size:  "))
for i in range(0,n):
    a=int(input("Enter no: "))
    list.append(a)
print(list)
if 4 in list:
    print("4 present in list")
else:
    print("not present")
    
######
list=[]
n=int(input("Enter list size:  "))
for i in range(0,n):
    a=int(input("Enter no: "))
    list.append(a)
print(list)
b=int(input("Enter Element : "))

if b in list:
    print("present")
else:
    print("not present")
    
    
    
#HW  take 10 no in a list insert some dublicate no write script to find dublicates

lst1= [10,20,30,20,10,50,60,40,80,50,40]
st1=set(lst1)
print(st1)
lst2=list(st1)
print(lst2)        


# take vovoles in a list and non volels in a list find out vovels in a list.

def vowles_present(list):
    vowles=[]
    for i in range(len(list)):
        if list[i]=='a' or list[i]=='e' or list[i]=='i' or list[i]=='o' or list[i]=='u':
            vowles.append(list[i])

    return vowles
list=[]
n=int(input("Enter list size:  "))
for i in range(0,n):
    a=(input("Enter vowels and non vowels: "))
    if len(a)==1:
        list.append(a)
    
        
  
print(list)
print(vowles_present(list))