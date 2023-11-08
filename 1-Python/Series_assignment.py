# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:05:25 2023

@author: SHRI
"""

#write a python program to create and  display a one dimentional array -like
#containing an array of data

import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)

#write a Pandas program to convert pandas module Series
# to Python list and it's types
#to_list method

import pandas as pd 
ds=pd.Series([2,4,6,8,10])
print("Pandas series and types :")
print(ds)
print(type(ds))
print("Convert Pandas series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

###############################################
#Write a Pandas program to add substract and multiple and divide 
#sample Series :[2,4,6,8,10] [1,3,5,7,8]
import pandas as pd

ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print("Add to series: ")
print(ds) 
ds=ds1-ds2
print("Subtract to series: ")
print(ds)
ds=ds1*ds2
print("multiply to series: ")
print(ds)
ds=ds1/ds2
print("Divide to series: ")
print(ds) 



#write a Pandas program to compare the element of the series
import pandas as pd

ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
print("Series 1: ")
print(ds1)
print("Series 2: ")
print(ds2)
print("Compare the element of the said series: ")
print("Equal: ")
print(ds1==ds2)
print("Greater than :")
print(ds1>ds2)
print("Less than:  ")
print(ds1 < ds2)


#Write a Pandas program to convert Dictionary to A pandas series.
# use can also pass list

import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':800}
print("Original Dictionary: ")
print(d1)
new_series=pd.Series(d1)
print("Converted Series: ")
print(new_series)



#Pandas program to convert a Numpy array to a series pandas
import numpy as np
import pandas as pd
n_a=np.array([10,20,30,40,50])
print("NumPy Array:  ")
print(n_a)
new_series=pd.Series(n_a)
print("Converted Pandas Series: ")
print(new_series)

#Write a pandas program to change the data type of 
#given column or a series

'''
Sample Series:
    Original Data Series:
    0  100
    1   200
    2 Python
    3 300.12
    4  400.00
    
ans: 
    
    0    100.00
    1    200.00
    2       NaN
    3    300.12
    4    400.00
    dtype: float64
    
'''

import pandas as pd
s1=pd.Series(['100','200','python','300.12','400.00'])
print("Original data Series:  ")
print(s1)
print("change the said data type to numeric: ")
s2=pd.to_numeric(s1, errors='coerce')
print(s2)


########################################################
#write a pandas program to convert the first column of a DataFrame as a series
#iloc syntex :  [: , :]
#[1:4,2:5]
import pandas as pd
d= {
    'col1':[1,2,3,4,7,11],
    'col2':[4,5,6,9,5,0],
    'col3':[7,5,8,12,1,11]
    
    }
df=pd.DataFrame(data=d) 
print("Original Series:")
print(df)
s1=df.iloc[:,0]  # all rows and oth columns
print("\n1st columns as a series: ")
print(s1)
print(type(s1))


##################################
##stack()- organise all list to one series 
#reset_index(drop=True)
# s=s.apply(pd.Series)
#s=s.stack()
#s=s.reset_index(drop=True)
import pandas as pd
s = pd.Series([
    ['Red','Green','White'],
    ['Red','Black'],
    ['yellow']
    ])

print("Original list series: ")
print(s)

#s=s.apply(pd.Series).stack().reset_index(drop=True)
s=s.apply(pd.Series)
s=s.stack()
s=s.reset_index(drop=True)
print("One Series: ")
print(s)


'''Dataframe - stack() function

The stack function is used to stack the prescribed level(s)
from columns to index
return 

''''''


#write pandas program to add some data
# to an existing series

'''
import pandas as pd
s= pd.Series(['100','200','python','300.12','400.00'])
print("Orininal Data series: ")
print(s)
print("\n Data Series after adding some data: ")
new_s=pd.concat([s,pd.Series([500,'php'])], ignore_index=True)
print(new_s)

#########################################################################


#write a pandas program to sort a given series
import pandas as pd
s= pd.Series(['200','100','python','300.12','400.00'])
print("Orininal Data series: ")
print(s)
new_s=pd.Series(s).sort_values()
print(new_s)

#write a Pandas program to change the order of index
#OF A given series
#reindex() method 

import pandas as pd
s =pd.Series(data=[1,2,3,4,5], index=['A','B','C','D','E'])
print("Orininal Data series: ")
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print("Data series after changing the order of index:")
print(s)
