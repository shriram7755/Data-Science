# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:27:59 2023

@author: SHRI
"""

'''
#what is numpy
#The NumPy library is popular open source Python library
#used for scientific computing application , and its stand for numerical in 
#python , which is consisting of multidimensional array
#object and collections of routines for processing  


'''
#install Python NumPy library
#pip install numpy


'''Write a Python list can cantain  different Data types within a single
list ,all the element in the numpy array are homogenous
'''

#arrays in numpy
#create ndarray

import numpy as np

arr=np.array([10,20,30])
print(arr)

#[10 20 30]

#Create a multidimensional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)


#Represent The minimum Dimensions
#use ndmin param to specify how many minimum 
#dimension you wanted to create an array with 
#minimum dimension

import numpy as np

arr=np.array([10,20,30],ndmin=3)   #its create 3D array
print(arr)
#[[[10 20 30]]]

#change the Datatype
#dtype parameter

arr=np.array([10,20,30],dtype=complex)
print(arr)      
#output
#[10.+0.j 20.+0.j 30.+0.j]


#GET the Dimension of Array

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)
print(arr)
print(arr) 

#Finding the size of each items in the array
arr=np.array([10,20,30])
print("Each Items Contain Bytes: ",arr.itemsize)




#finding the Datatype of Each array Item
#
arr=np.array([10,20,30])
print("Each Items of type : ",arr.dtype)



#Get the Shape and size of Array

arr=np.array([[10,20,30,40],[50,60,70,80]])
print("Array Size :",arr.size)
print("Array Shape :",arr.shape)


#Create a Sequance of Integer using arrange()
#create a sequance of Integer

arr=np.arange(0,20,3)
print("The sequance of array with step of 3\n: ",arr) 
''':  [ 0  3  6  9 12 15 18]'''

#Access single element using index 
arr=np.arange(11)
print(arr)

print(arr[2])

print(arr[-2])

#Multidemensional Array Indexing

arr=np.array([[10,20,30,40,50],[50,60,70,80,90]])
print(arr)

'''
[[10 20 30 40]
 [50 60 70 80]]
'''

#shape
print(arr.shape)
'''
(2, 4)
'''

#access 2d array element
print(arr[1,1])   #60

print(arr[0,4])   # 50

print(arr[1,-1])  #90

#Access array element element using slicing

arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)          #[2 4 6 8]

x=arr[-2:3:-1]
print(x)          #[8 7 6 5]

x=arr[-2:10]
print(x)          #[8 9]

#slicing of array

multi_arr=np.array([[10,20,30,40],
                    [40,50,60,70],
                    [60,10,70,80],
                    [30,90,40,30]
                    ])
multi_arr
#for multidimensional Numpy array
#you can access the elements as below

multi_arr[1,2] #TO access the value at row 1 and columns 2
multi_arr[1,:]
multi_arr[:,1] #TO access the value all row 1 and columns 1

x=multi_arr[:3,::2] #colums from 0 to 3 and rows 
x
'''array([[10, 30],
       [40, 60],
       [60, 70]])
'''

#Integer array  Indexing

arr=np.arange(35).reshape(5,7) # 5 rows and 7 Colums
print(arr)
'''
[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]
'''

#Boolean array Indexing
#used in ML model design

arr=np.arange(12).reshape(3,4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

rows=np.array([False,True,True])
wanted_rows=arr[rows, :]
print(wanted_rows)
'''
[[ 4  5  6  7]
 [ 8  9 10 11]]
'''

# Convert one dimensional array

#create array
array=np.array([10,20,30,40])
print("Array",array)      #Array [10 20 30 40]
print(type(array))        #<class 'numpy.ndarray'>

Convert to list 

lst= array.tolist()
print("list",lst)        #list [10, 20, 30, 40]
print(type(lst))         #<class 'list'>

#Convert multidimensional array to list

array=np.array([[10,20,30,40],
                    [40,50,60,70],
                    [60,10,70,80],
                    [30,90,40,30]
                    ])
print("array:",array)

lst= array.tolist()
print("list",lst)
'''
list [[10, 20, 30, 40], [40, 50, 60, 70], [60, 10, 70, 80], [30, 90, 40, 30]]
'''

#Convert python list to array in python
#2 method

#numpy.array()
#numpy.asarray()

#crate a list
list=[20,30,40,50]

#convert array
array=np.array(list)
print("Array: ",array)     #Array:  [20 30 40 50]


#use asarray():
  
#crate a list 
list=[20,30,40,50]

#convert array 
array=np.asarray(list)
print("Array: ",array)       #Array:  [20 30 40 50]

# Numpy Array properties
     #ndarray.shape
     #ndarray.ndim
     #



#resize of array
array=np.array([[1,2,3],[4,5,6]])
array.shape=(3,2)
print(array)
'''
[[1 2]
 [3 4]
 [5 6]]
'''

#Reshape array
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
print(new_array)
'''
[[1 2]
 [3 4]
 [5 6]]
'''



