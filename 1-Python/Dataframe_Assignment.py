# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:01:55 2023

@author: SHRI
"""

"""write a pandas programn to create a datafrane from dictionary and display 
sample data :{'X':[78,85,96,80,86], 'Y':[84,94,89,83,86], 'Z':[86,97,96,72,83]} 
"""

import pandas as pd
d={'X':[78,85,96,80,86],
    'Y':[84,94,89,83,86],
    'Z':[86,97,96,72,83]
    }

df=pd.DataFrame(d)
print(df)
df.dtypes

'''
Write a pandas program to create and display A Dataframe from the specific  dictionary data which has 
Sample Python dictionary data and list  lables:
    exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
                'score':[12.5,9,16.5,np.nan,9,20],
                'attempt':[1,3,2,3,2,3],
                'qualify':['yes','no','yes','no','yes','no'],
                
               }
    lables=['a','b','c','d','e','f']
    
'''
import pandas as pd

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,NaN,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df

print("Summary of the basic information about the dataframe and its ")
print(df.info())
df.describe()


#----------------------------------------------------------------------------------------------
#write a pandas program to display first three row of the dataframe

 import pandas as pd
 import numpy as np
 
 exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
    'score':[12.5,9,16.5,np.nan,9,20],
    'attempt':[1,3,2,3,2,3],
    'qualify':['yes','no','yes','no','yes','no'],
    }
 lables=['a','b','c','d','e','f']

 df=pd.DataFrame(exam_data, index=lables)
 df
 
 print("First three row of the dataframe : ")
 print(df.iloc[:3])


#-------------------------------------------------------------------------------------
#Write a pandas program to select the 'name' and 'score' columns from dataframe
 import pandas as pd
 import numpy as np
 
 exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
    'score':[12.5,9,16.5,np.nan,9,20],
    'attempt':[1,3,2,3,2,3],
    'qualify':['yes','no','yes','no','yes','no'],
    }
 lables=['a','b','c','d','e','f']

 df=pd.DataFrame(exam_data, index=lables)
 df
 
 print("select the 'name' and 'score' columns : ")
 print(df[['Name','score']])

#--------------------------------------------------------------------------------------------
#write a pandas program  to  select the specific column and rows from the a dataframe
'''
Expected output
   score qualify
a   12.5     yes
b    9.0      no
c   16.5     yes
d    NaN      no
e    9.0     yes
f   20.0      no

'''
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df

print(" select the specific column and rows : ")
print(df[['score','qualify']])




#----------------------------------------------------------------------------------------------------
#write a pandas program to select row where the number of attempt
#in the examination is greater than 2

import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
print(" number of attempt in the examination is greater than 2: ")
print(df[df['attempt']>2])


df2=df.loc[df.attempt>2]
df2


#------------------------------------------------------------------------------------------
#write a pandas program to count the no of rows ans columns 
#of a Dataframe

import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
#find total rows
total_rows=len(df.axes[0])
print(total_rows)

#find total columns
total_columns=len(df.axes[1])
print(total_columns)

print("Number of Rows: "+str(total_rows))
print("Number of Colums: "+str(total_columns))


#-----------------------------------------------------------------------------------------------
#write a pandas program to select the row where the score is missing
#i.e Nan
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
print("Rows where score is missing: ")
df2=(df[df['score'].isnull()])

#------------------------------------------------------------------------------------------------
#Write a search pandas program to select the row the score is between 15 to 20(inclusive)
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)

print("row the score is between 15 to 20 : ")
df2=(df[df['score'].between(15,20)])


#-------------------------------------------------------------------------------------------------
#write a pandas program to select  the rows where the no of attempts in the examination is
#less than 2 and score is greater than 15

import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)

print("no of attempts in the examination is less than 2 and score is greater than 15 : ")
df2=(df[(df['attempt']<2) & (df['score']>15)])
print(df2)

#------------------------------------------------------------------------------------------------
#write a pandas program to change  the score in row 'd' to 11.5
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)

print("\n Change the score in row 'd' to 11.5 :")
df.loc['d', 'score'] = 11.5  #null value change to 11.5
print(df)


#----------------------------------------------------------------------------------------------
#write a pandas program to calculate 
#sum of the examination attempts by the students
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)

print("sum of the examination attempts by the students: ")
print(df['attempt'].sum())

#----------------------------------------------------------------------------------------------------
#Write a search pandas program  to
#to calculate the mean of all styudents score

import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)

print("\nto calculate the mean of all styudents score:  ")
print(df['score'].mean())

#----------------------------------------------------------------------
# write a pandas program to  append a new row
#'k' to the dataframe with gives  values for each column

import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)

print("original rows: ")
print(df)
print("\n Apppend a new rows: ")
df.loc['k']=['suresh', '20.5','2','yes']
print("print all records after the insert a new records: ")
print(df)

#--------------------------------------------------------------------
#write a pandas program to sort the dataframe 
#first by 'name' in descending order ,
#then by 'score' in asecending order.


import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
print("original rows: ")
print(df)
df =df.sort_values(by=['Name'] , ascending=[False])
print(df)
df =df.sort_values(by=['score'] , ascending=[True])
print(df)
print("sort the dataframe first by 'name' in descending order ,then by 'score' in asecending order")
print(df)

#------------------------------------------------------------------------------
#Write pandas program to replace the 'qualify ' column conatains the values 
#'yes' and 'no' with True and falsee
#iMP in project development
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
print("original rows: ")
print(df)
print("\n to replace the 'qualify ' column conatains the values 'yes' and 'no' with True and false : ")
df['qualify']=df['qualify'].map({'yes':True, 'no': False})
print(df)


#---------------------------------------------------------------------------------
#Write a pandas program to change the name 
#'Rohit' to 'James' in name colums of the dataframe.

import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
print("original rows: ")
print(df)
print("\n Change the name 'Ram' to Shri: " )
df['Name']=df['Name'].replace('Ram', 'Shri')
print(df)

#-----------------------------------------------------------------------------------
#Write a pandas program to insert 
#a new columns in existing dataframe
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
print("original rows: ")
print(df)
print("\n To insert a new columns in existing dataframe: " )
color=['Red','Blue','Orange','Red','White','Blue']
df['color']=color
print("\nto insert a new columns in existing dataframe")
print(df)
#------------------------------------------------------------------------------
#Write a pandas program  to iterate over rows in a Dataframe
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[16,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df

for index,row in df.iterrows():
    print(row['Name'], row['score'])
    
    
#------------------------------------------------------------------------------
#Write a pandas program to get list from Dataframe columns headers
