s# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:05:01 2023

@author: SHRI
"""

import numpy as np
print(np.__version__)

#---------------------------------------------------------------
#Write a numpy program to test wheather
#none of the element of a given array are zero
#np.all(arrayname)

import numpy as np

x=np.array([1,2,3,4])
print("Original array :")
print(x)
print("test wheather none of the element of a given array are zero: ")
print(np.all(x) )                  #True

                 
x=np.array([0,1,2,3])
print("Original array: ")
print(x)
print("test wheather none of the element of a given array are zero: ")
print(np.all(x))                  #False


#write a numpy program to rest any of the element in the numpy array 
#are non zero

x=np.array([1,2,3,4])
print("Original array :")
print(x)
print("test wheather none of the element of a given array are non zero: ")
print(np.any(x))   #True

x=np.array([0,0,0,0])
print("Original array: ")
print(x)
print("test wheather none of the element of a given array are non zero: ")
print(np.any(x))  #False


#write a Numpy program to test a given array element-wise for finiteness
#(not a infinity or not a number) VIMP

import numpy as np
a=np.array([1,0,np.nan,np.inf]) 
print("Original array :")
print(a)

print("Test a given array element-wise for finiteness: ")
print(np.isfinite(a))    #[ True  True False False]


#--------------------------------------------------------------------------
#write a numpy program to test element-wise for NaN of a given array
#IMP 
import numpy as np
a=np.array([1,0,np.nan,np.inf]) 
print("Original array :")
print(a)

print("Test element-wise for NaN: ")
print(np.isnan(a))    #[False False  True False]

#----------------------------------------------------------------------------
Write a program  to create an element-wise comparison 
#(greater ,greater_equal,less and less_equal and less_equal) of two given array

import numpy as np

x=np.array([3,5])
y=np.array([2,5])
print("Original array: ")
print(x)
print(y)

print("Comparison greater: ")
print(np.greater(x,y))   #[ True False]

print("Comparison greater_Equal: ")
print(np.greater_equal(x,y)) #[ True  True]

print("Comparison less: ")
print(np.less(x,y))         #[False False]

print("Comparison less_equal: ")
print(np.less_equal(x,y))   # [False  True]

# --------------------------------------------------------------------------
#write a numpy program to create 3*3 matrix

import numpy as np
array_2D=np.identity(3)
print("3*3 Matrix : ")
print(array_2D)   

'''
print(array_2D)                         
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
#--------------------------------------------------------------------------
#write a numpy program to generate a random number between
#o and 1

import numpy as np
rand_num=np.random.normal(0,1,2)
print("Random number bet 0 and 1: ")
print(rand_num)                   
'''[-0.27375265  0.95604502] '''

#---------------------------------------------------------------------------
# write a pandas program to create a 3*4 array and iterate over it

import numpy as np
a=np.arange(10,22 ).reshape(3, 4)
print("Original array :")
print(a)

print("Each element of the array is: ")
for x in np.nditer(a):
    #print(x)
    print(x, end=" ")
    print()


#----------------------------------------------------------------------------
#write a numpy program to create a
#vector of length 5  with values 
#evenly distibuted between 10 and 50

import numpy as np
v=np.linspace(10, 49,5)
#10-start point ,49-end point , 5 nos in vector
print("vector of length 10  with values evenly distibuted between 5 and 50")
print(v)    #[10.   19.75 29.5  39.25 49.  ] 


#-----------------------------------------------------------------------------
#Write a numpy program to create a 3*3 matrix
#with value ranging from 2 to 10

import numpy as np
x=np.arange(2, 11).reshape(3, 3)
print(x)
'''
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
'''

#-----------------------------------------------------------------------------
Writa a numpy program to reverse an array 
# the first element become last
import numpy as np
x=np.arange(12, 38)
print("Original array :")
print(x)
print("Reverse array :")
x=x[::-1]
print(x)
'''
[37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14
 13 12
'''
#-------------------------------------------------------------
#write a numpy program to compute the multiplication of 
#two matrix

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original matrix: ")
print(p)
print(q)
result=np.dot(p,q)
print("Result of the said matrix multiplication :")
print(result)
'''
[[1 2]
 [3 4]]
'''

#----------------------------------------------------------------
#Write a numpy program to compute the cross product of 
#two matrix 
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original matrix: ")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)

print("numpy program to compute the cross product of two matrix:")
print(result1)      #[ 2 -3]
print(result2)      #[-2  3]


#-------------------------------------------------------------------
#write a numpy program to compute the determinant of given 
#square array

import numpy as np

from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("Original 2-D Array: ")
print(a)
print("Determinant of 2-D array ")
print(np.linalg.det(a))  #2.0


#-----------------------------------------------------------------
#Write a numpy program to find out eigen values and eigen vector 
# of given square array

import numpy as np
m=np.mat("3 -2;1 0")
print("Original matrix: ")
print("o/p",m)

w,v =np.linalg.eig(m)
print("Eigen Values : ",w)  #Eigen Values :  [2. 1.]
print("Eigen vector : ",v)   #Eigen vector :  [[0.89442719 0.70710678]
                                           # [0.4472136  0.70710678]]


#----------------------------------------------------------------
#Write a numpy program to compute 
#the inverse of  a given matrix

import numpy as np
m=npw

