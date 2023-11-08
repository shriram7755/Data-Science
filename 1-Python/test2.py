# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:05:50 2023

@author: SHRI
"""

'''
Q.1
Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df=pd.DataFrame(exam_data,index=labels)
df
#df['qualify']=df['qualify'].replace(['yes'],'True')
#['qualify']=df['qualify'].replace(['no'],'Flase')
df['qualify']=df['qualify'].replace(['yes','no'],['True','Flase'])
df


'''
Q2Write a Python program to plot two or more lines  with different styles. 
'''


import matplotlib.pyplot as plt
import  numpy as np

y=np.arange(1, 3, 0.2)

plt.plot(y, 'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s');
plt.show()




'''
Q.3 Create an array[1,2,3] write L1 and L2 norm value for it
'''

import numpy as np
arr=np.array([1,2,3])
l1=np.linalg.norm(arr,1)
l2=np.linalg.norm(arr,2)
print(l1)
print(l2)
'''
Q.4 Write a NumPy program create [[1, 0], [1, 2]] square array and  compute 
the determinant of a given square array.
'''
import numpy as np
arr=np.array([[1,0],[1,2]])
#arr=np.array([[1,0],[1,4]])
det=np.linalg.det(arr)
print(int(det))

'''
Q.5 Write a Python function to find the kth smallest element in a list.
'''
lst=[22,10,12,45,66,4,7,9]
'''
a=int(input('Enter the size of list:'))
for i in range(a):
    print("Enter element:")
    lst.append(i)
print(lst)
'''
def small_no(a):
    a.sort()
    return a[0]

small_no(lst)




