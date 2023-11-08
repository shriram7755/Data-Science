# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:39:23 2023

@author: mobin
"""

###########################Panda#############################
"""
Series is used to model 1dimension data, 
similar to a list in pyton.
The series object also has few more bits of data,
including an index and name.
series also haveing index and name

"""

import pandas as pd
songs2 = pd.Series([145, 142, 38, 13],name='counts')
#It is easy to inspect the index of a series
songs2.index
#The index can be string based as well,
#in which case pandas indicates
#that the data type for the index is object(not string)

import pandas as pd
songs3 = pd.Series([145, 142, 38, 13],name='counts',
                   index=['mobin','shaikh','khan','pathan'])
songs3.index
songs3

############################################
"""
The NaN value
This value stands for not A number, and is usually
ignored in arithematic operations.(Similar to NULL in SQL).
If you load data from a CSV file, an empty value for an 
otherwise 
numeric column will became NaN

"""
import pandas as pd
f1 = pd.read_csv('c:/1-python/age.csv.xls')


import pandas as pd
f1=pd.read_csv('age.csv.xls')

##################################################
import pandas as pd
f1=pd.read_csv('age.csv.xls')


df=pd.read_excel('c:/1-python/Bahaman.xlsx')


##################################################
#Numpy
"""
None, NaN, nan, and null are synonyms .The Series object
behaves similarly to a NumPy array.
"""
import numpy as np
numpy_ser = np.array([145, 142, 38, 13])
songs3[1] #accessing series

numpy_ser[1]
#They both have methods in common
songs3.mean()
numpy_ser.mean()

##########################################################

#Creation
shaikh= pd.Series([10, 7, 1, 22],
                  index=['1968','1969','1970','1971'])
name='Shaikh Songs'
shaikh

#####################################
#Reading 
#To read or select the data from a series

shaikh['1968']
shaikh['1970']
#We can iterate over data in a series as well. 
#when iterating over a series

for item in shaikh:
    print(item)
##############################################
"""Updating-
Updating values in series can be a little tricky as well.
To update a value for a given index lable,
the standard index assignment operation works

"""

shaikh['1969']=68
shaikh['1969']

"""Deletion-
The del statement appears to have problems 
with duplicate index

"""

s= pd.Series([2, 3, 4], index=[1, 2, 3])
del s[1]
s

###########################################

#Convert types
"""
string use.astype(str)
numeric use pd.to_numeric
integre use .astype(int)
note that this will fail with NaN
date time use pd.to_datetime
"""
import pandas as pd
songs_66 = pd.Series([3, None, 11, 9],
                     index=['George','Ringo','John','Paul'],
                     name='counts')
songs_66.dtypes
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
#There will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#If we pass errors='coerce',
#we can see that it supports many formats
songs_66.dtypes
#dealing with None
#The .fillna method will replace them with a given value
songs_66.fillna(-1)
#Nan values can be dropped from
#the series using .dropna
songs_66.dropna()
###################################################

#Append, combining, and  joining two series

import pandas as pd
songs_69 = pd.Series([7, 16, 21, 39],
                     index=['Ram','Sham','Ghansham','Krishna'],
                     name='counts')
#To concatenate two series together,simply use the .append

songs=songs_66.append(songs_69)


#PLotting series

import matplotlib.pyplot as plt
fig = plt.figure()#will open canvas for figure
songs_69.plot()
plt.legend()

#Bar graph

import matplotlib.pyplot as plt
fig = plt.figure() 
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()#For scale on graph

############################################
#Histogram

import numpy as np
data = pd.Series(np.random.randn(500),name='500 random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
























