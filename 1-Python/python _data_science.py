# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:11:10 2023

@author: SHRI
"""

#settings
#tools - preferences- ipython console - graphics - graphics backent -select automatic


#Python for Data Science
1)Pandas
2)MatplotLib  - visualization 
3)Numpy
4)Seaborn

# a series is used to model one dimensional data,
# similar to a list in python
# The  series object also has a few more bits
# of data, including an #index and a name

#step 1) Import pandas

import pandas as pd
songs2= pd.Series([145,142,38,13],
                  name='counts')    

songs2.index 

#The index can be  string based as well,
#in which case pandas  indicates,
#that the datatype for the index is object(not string)

import pandas as pd
songs3= pd.Series([145,142,38,13],name='counts',
                  index=['Paul','John','George','Ringo'])
songs3.index 
songs3



#The NaN Value
# This value stands for Not a Number
#and it is usually  ignored in arithmatic
#opration.(similar to NULL in SQL)

#if working directry is not selected the you are to  give absolute path.

#numeric column will become NaN.
import pandas as pd
f1=pd.read_csv('c:/1-Python/age2.csv') # absoulate path
f1

df=pd.read_excel('c:/1-Python/Bahaman.xlsx')

#None , NaN, nan and null are synonyms 
#The series object behaves similarly to 
# a numPy Array
import numpy as np
numpy_ser=np.array([145,142,38,13])

#142
numpy_ser[1]
numpy_ser[3]
numpy_ser.mean()


#Pandas series data structure provides
#support for the basic crud
#operation -create ,read ,update,and delete.
#creation

george=pd.Series([10,7,1,22],
index=['1978','1999','1992','1992'],
name='George Songs')
george


#The previous example illustrates an 
#interesting feature of pandas-the
#index value are string and they
# are not unique





#reading
# to read and select the the data from the series
george['1978']


george['1999']


#iterating over series

for item in george:
    print(item)
    
    
#Updating value in series 

george['1978']=68
george['1978']

#Delating value in Series

s=pd.Series([2,3,4], index=[1,2,3])
del s[1]
s

#convert types 
#string use.astype(str)
#numeric use pd.to_numeric
#integer use .astype(int)
#note that this will faiul to NaN
#datetime use pd.to_datetime

import pandas as pd

songs_66 = pd.Series([3,None,11,9],
index=['George','Ringo','John','Paul'],
name='counts')
songs_66.dtypes
#dtypes('float64')
pd.to_numeric(songs_66.apply(str))
#There will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass error='coerce
#we can see that it support many formats
songs_66.fillna(-1)   #use in ML model 

songs_66.fillna(-1)

songs_66.dropna()


########################################################
#Append , Combaining , and Joining two series

songs_69 =pd.Series([7,16,21,39],index=['George','Ringo','John','Paul'],name='counts')

songs=songs_66.append(songs_69)



################################################
#ploting  series
import matplotlib.pyplot as plt

fig =plt.figure()

songs_69.plot()
plt.legend() 

#######################################################
#bar Graph
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar', color='r')
plt.legend() 


########################################################
#Histogram
import pandas as pd
import numpy as np
data=pd.Series(np.random.randn(500),name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

#Upgrate Pandas to Latest or Specific version
#on base terminal write
#conda install --upgrade pandas
#conda install -c anaconda pandas

#Upgrade pandas to Latest or Specific version
# conda update pandas==2.0.3

# to  check the version of pandas
import pandas as pd
pd.__version__

#create using constructer
#create pandas Dataframe from list
import pandas as pd
technologies=[["Spark",2000,"30days"],
              ["pandas",20000,"40days"]]

df=pd.DataFrame(technologies)
print(df)

#Since we have not given lables to columns and
#indexes,Datafreame by default assign
#incremental sequances number as lables
#to both the rows and columns , these are called index .
#add column & row lables to the dataframe

column_names=["Courses ","fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

#-------------------------------------------------------------------------
df.dtypes
###########################################




##############################################################################
"""You can also assign custom data types to columns.
set custom types to DataFrame
"""

import pandas as pd
technologies= {
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas","Oracel","Java"],
    'Fee' :[20000,25000,26000,27000,28000,29000,21000],
    'Duration' :['30days','40days','50days','60days','70days','80days','90days'],
    'Discount' :[11.8,21.8,31.8,41.8,51.8,61.8,71.8]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

#Convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)

#Change All columns to same type
df=df.astype(str)
print(df.dtypes)

#Change type for one or multiple columns

df = df.astype({"Fee": int, "Discount": float})
print(df.dtypes)


# Convert Data type to all  column in a list  #IMP in Interview
df=pd.DataFrame(technologies)
df.dtypes
cols=["fees","Discount"]
df[cols]=df[cols].astype('float')
df.dtypes


#ignore  Errors
df=df.astype({"Courses":int},errors='ignore')
df.dtypes

#Generator Errors
df=df.astype({"Courses":int},errors='raise')
df.dtypes


#Convert feed column to numeric  type
df =df.astype(str)
print(df) 

 



#------------------------------------------------------------------------------------------------------------------
#Create a DataFrame from Dictionary
import pandas as pd
technologies =  {
    'Courses':['Spark','PySpsrk','Hadoop'],
    'Fees':[20000,25000,26000],
    'Duration':['30Days','40Days','35Days'],
    'Discount':[1000,1500,1700]
    }

df=pd.DataFrame(technologies)
df

#convert Dataframe to csv
df.to_csv('technologies.csv')

#Create a DataFreame From CSV File
df=pd.read_csv('technologies.csv')


#---------------------------------------------------------------------------------------------------------------------
# Pandas DataFreame - Basic Operation
#Create a DataFreame (properties )
#IMP 

import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas",None,"Oracel","Java"],
    'Fee' :[20000,25000,26000,27000,28000,np.nan,29000,21000],
    'Duration' :['30days','40days','50days','60days','70days','','80days','90days'],
    'Discount' :[1000,2000,3000,4000,5000,6000,7000,8000]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)


##################################################
#DataFrame Properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes


#Accessing one column contents []
df['Fee']
#Accessing two column contents [[]]
df[['Fee','Duration']]
#select certain rows and assign it to another dataframe      [ row:   ,  :col]
df2=df[6:]  # 6 and 7 row and all column
df2

#######################################
#accessing certain cell from column 'Duration'
df['Duration'][3]

#substracting specific value from column
df['Fee']=df['Fee']-500
df['Fee']

#Pandas to Manipulate DataFrame
#Describe Dataframe
#Describe DataFrame for all specific columns
df.describe()  # describe() - its only show int and float values not object
#it will show 5 Number summary

#------------------------------------------------------------------------------------------
#rename() -Rename the pandas DataFrame column
df=pd.DataFrame(technologies, index=row_labels)

#Assign the new Header by setting new columns names
df.columns=['A','B','C','D']


#Rename columns name using rename() method
#accessing row - axis=0
#accessing columns - axis=1 another option axis='columns'
df=pd.DataFrame(technologies, index=row_labels)
df.columns=['A','B','C','D']
df2= df.rename({'A':'c1','B':'c2'}, axis=1)
df2= df.rename({'C':'c3','D':'c4'}, axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})


#---------------------------------------------------------------------------------------------------


#Drop dataframe Rows and Columns
df=pd.DataFrame(technologies,index=row_labels)

#Drop rows and columns by lables

df1=df.drop(['r1','r2'])

df1

df1=df.drop(df.index[1])  
df1

df1=df.drop(df.index[[1,3]]) # for drop specific  rows  use 2 ractange brackets [[   ]]


#Delete Row By index range

df1=df.drop(df.index[2:])    # two onwards rows are deleted



#when you have default indexs for rows 
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1

df=pd.DataFrame(technologies)
df1=df.drop([0,3])    # it will delete row0 and row3
df1=df.drop(range(0,2))  # it will delete 0 and 1



#--------------------------------------------------------------------------------------
#Droping of columns
# when you are dropping column by names then its is mandetory to mention axis=1

import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas",None,"Oracel","Java"],
    'Fee' :[20000,25000,26000,27000,28000,np.nan,29000,21000],
    'Duration' :['30days','40days','50days','60days','70days','','80days','90days'],
    'Discount' :[1000,2000,3000,4000,5000,6000,7000,8000]
    })

df = pd.DataFrame(technologies)
print(df)
#drop column by name
#Droop 'fee' Column
#axis=1 for columns

df2=df.drop(['Fee'],axis=1)


#Explicitely using parameter name 'lables'

df2=df.drop(labels=["Fee"], axis=1)


#alternatively you can also use column insted of labels

df2=df.drop(columns=["Fee"], axis=1)


#Drop Colums by index


print(df.drop(df.columns[1], axis=1))

###################################
df = pd.DataFrame(technologies)

#using inplace=True
#when we are working on  original dataframe the write inplace=True.
df.drop(df.columns[1], axis=1, inplace=True) 
print(df)

########################################

df = pd.DataFrame(technologies)
df2=df.drop(["Courses","Fee"],axis=1)
print(df2)
#drop two or more columns by Label Name
df2=df.drop(["Courses","Fee"],axis=1)


#Drop Two or more columns by index

df = pd.DataFrame(technologies)
df2 = df.drop(df.columns[[0,1]], axis=1)
print(df2)

#################################
#Drop Columns from list of columns

df = pd.DataFrame(technologies)
df.columns # find all the columns in the dataframe 
lisCol = ["Courses","Fee"]   # remove specific columns 
df2=df.drop(lisCol,axis=1)
print(df2)




############################################################################################

#Pandas Select Row by Index (Position/Label) 
import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas",None,"Oracel","Java"],
    'Fee' :[20000,25000,26000,27000,28000,np.nan,29000,21000],
    'Duration' :['30days','40days','50days','60days','70days','','80days','90days'],
    'Discount' :[1000,2000,3000,4000,5000,6000,7000,8000]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)

#df.iloc[startrow:endrow ,startcolumn:endcolumn]
df = pd.DataFrame(technologies, index=row_labels)
#Below are quick example
df2=df.iloc[:,0:2]
df2
#this line gives the slicing operator to get Dataframe   iloc and loc
#item by Index
# The first slice [:] indicates to return all rows.

df = pd.DataFrame(technologies, index=row_labels)
df2=df.iloc[0:2,:]  # o and 2 rows and all columns
df2


# for some row and some columns
df = pd.DataFrame(technologies, index=row_labels)
df2=df.iloc[1:2,1:3]  #
df2


#The Second operator [1:3] yield columns1 and columns2 
#select Row by Integer Index 
df2=df.iloc[2]  #
df2


df2=df.iloc[[2,3,6]] #accessing miltiple row data its need to '[[ 2,3,6 ]]' 
df2

df2=df.iloc[1:5]
df2=df.iloc[:1] 
df2=df.iloc[:3]
df2=df.iloc[-1:]
df2=df.iloc[-3:]
df2=df.iloc[::2]      



#select row by Index lables
# in label its covers all r1 to r5 rows  #df2=df.loc["r1":"r5"]

df2=df.loc["r2"]
df2=df.loc[["r2","r3","r6"]]
df2=df.loc["r1":"r5"] 
df2=df.loc["r1":"r5":2]




#################################################################################

import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas",None,"Oracel","Java"],
    'Fee' :[20000,25000,26000,27000,28000,np.nan,29000,21000],
    'Duration' :['30days','40days','50days','60days','70days','','80days','90days'],
    'Discount' :[1000,2000,3000,4000,5000,6000,7000,8000]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)

#pandas Select Columns by Name and Index
# by Using df[] Notation
df2=df['Courses']
#Select Multiple columns
df2=df[['Courses','Fee','Duration']]

#Using loc[] to take columns slices
#loc[] syntex to Slice Columns
#df.loc[;,start:stop:step]
##select Multiple Columns
df2=df[ :, ['Courses','Fee','Duration']]

#selectRandom number
df2=df[ :, ['Courses','Fee','Duration']]

#select  Columns between two columns
df2=df[ :, ['Courses':'Discount']
    
#select column by range
df2=df.loc[:,'Duration':]
#select columns by range
#All the columns upto 'Duration'
df2=df.loc[:,:'Duration']
       


#---------------------------------------------------------------------------------------
08/08/2023
#Pandas.Dataframe.query() by Example
import pandas as pd
import numpy as np 
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,27000,28000],
    'Duration' :['30days','40days','50days','60days','50days'],
    'Discount' :[1000,2000,3000,4000,5000]
    })

df = pd.DataFrame(technologies)
print(df)
# Query all rows with  courses equal to spark
df2=df.query("Courses=='Spark'")

#not equal condition
df2=df.query("Courses!='Spark'")

#-------------------------------------------------------------------
#Pandas Add Columns to Dataframe
import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,27000,28000],
    'Duration' :['30days','40days','50days','60days','50days'],
    'Discount' :[0.1,0.2,0.3,0.4,0.5]
    })

df = pd.DataFrame(technologies)
print(df)

#ADD new columns to the dataframe
tutors=["Ram","Sham","Ghansham","Ganesh","Ramesh"]
df2=df.assign(TutorsAssigned=tutors)
print(df2)

#Add Multiple Column to the Dataframe
MNCCompanies=['TATA','HCL','Infosys','Google','Amazon']
df2=df.assign(MNC=MNCCompanies,TutorsAssigned=tutors)
print(df2)

 
#Derive new columns from existing columns
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x:x.Fee*x.Discount/100)
print(df2)


#Append Columns to the Existing Pandas Dataframe
#Add new columns to the  Existing Pandas Dataframe
df=pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
print(df)

#Add new Columns to the Specific Position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)

#--------------------------------------------------------------------------
#quick Example of get the Number of rows in Dataframe
row_count=len(df.index)
row_count

row_count=len(df.axes[0])
row_count

column_count=len(df.axes[1])
column_count

#----------------------------------------------------------------------------
df=pd.DataFrame(technologies)
row_count=df.shape[0]    #return no of columns
row_count
column_count=df.shape[1] #return no of rows
column_count




#----------------------------------------------------------------------------
#pandas Apply function to a columns
#Below are quick example
# using Dataframe.apply() to apply function add columns

import pandas as pd
import numpy as np

data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }

df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3 

df2=df.apply(add_3)    #add 3 to all  columns 
df2


#apply mathematical operation to specific columns 

df2=((df.A).apply(add_3))  #  syntax 


#Using apply function Single Columns
def add_4(x):
    return x+4 

df["B"]=df["B"].apply(add_4)
df["B"]


#Apply to Multiple Columns 
#when you are apply both the Columns then you need to pass list of columns 

df[['A','B']]=df[['A','B']].apply(add_4)
df

df[['A','B','C']]=df[['A','B','C']].apply(add_4)
df

#Apply Lambda function to each columns

df2=df.apply(lambda x:x +10)
df2

#lambda function to Specific  columns 
df2=df['A']=df['A'].apply(lambda x:x +10)
df2

#using pandas.Dataframe.transform() to Apply Function Columns
using Dataframe.transform()

def add_2(x):
    return x+2
df=df.transform(add_2)
df

#USing pandas.Dataframe.map() to single Column

df['A']=df['A'].map(lambda A:A/2.)
df


#using Numpy Function to single Columns
# USing Dataframe.apply() & [] operator 

import numpy as np

data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }

df=pd.DataFrame(data)
print(df)

#square of a column
df['A']=df['A'].apply(np.square)
print(df)

#Using Numpy.square() method
#using numpy.square() and [] operator 
df['A']=np.square(df['A'])
print(df)

#pandas groupby()  with example 

import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas","Hadoop","Spark","Pyspark"],
    'Fee' :[20000,25000,26000,27000,28000,np.nan,29000,21000],
    'Duration' :['30days','40days','50days','40days','70days','','30days','90days'],
    'Discount' :[1000,2000,3000,4000,5000,6000,7000,8000]
    })

df = pd.DataFrame(technologies) 
print(df)

#groupby()
df2=df.groupby(['Courses']).sum()
df2

#Group by multiple columns

df2=df.groupby(['Courses','Duration']).sum()
df2


#Add Index to the grouped data
#Add Row Index to the group by result

df2=df.groupby(['Courses','Duration']).sum().reset_index()
df2


#----------------------------------------------------------------------- 

#`Pandas get Columns Names from Dataframe

import pandas as pd
import numpy as np
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,27000,28000],
    'Duration' :['30days','40days','50days',None,np.nan],
    'Discount' :[0.1,0.2,0.3,0.4,0.5]
    })

df = pd.DataFrame(technologies)
print(df)

df.columns

#get the list of columns names from header
columns_header= list[df.columns.values]
print("The Columns header :",columns_header)

#Using list(df) to get the columns headers as a list
column_headers=list(df.columns)
column_headers




#---------------------------------------------------------------------------
#pandas Suffle Dataframe Rows
#df.sample(frac=1) or full rows
#df.sample(frac=0.5) or half rows
import pandas as pd
technologies= ({
    'Courses' :["Spark","Pyspark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,27000,28000],
    'Duration' :['30days','40days','50days','60days','45days'],
    'Discount' :[0.1,0.2,0.3,0.4,0.5]
    })


df=pd.DataFrame(technologies)
print(df)

#Pandas suffle Dataframe ROWS
#Suffle the dataframe rows &return all rows

df1=df.sample(frac=1)
print(df1)


df1=df.sample(frac=0.5)   #half entities
print(df1)

#Create a new Index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)


#Drop Suffle Index
#drop=True : reset index will delete the index insted of inserting 
#of inserting it back into the columns of the dataframe 
##drop=True : current index will be deleted entirely and numeric index re
#replace it

df1=df.sample(frac=1).reset_index(drop=True)
print(df1)
 
#--------------------------------------------------------------------
#Joins
import pandas as pd

technologies={
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30Days','40Days','35days','50Days'],
    
    }

index_lables1=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_lables1)
df1
technologies2={
    'Courses':["Spark","Java","Python","Go"],
    "Discount":[2000,2300,1200,2000]
    }
index_lables2=['r1','r6','r3','r5']

df2=pd.DataFrame(technologies2,index=index_lables2)
df2

#pandas join, by default it will join the table left join
#join - horizontally join   #IMP
#in Concatination - veritically Join
#It is used to join two dataframe  on index 
#When the index dont match the rows gets dropped from both dataframe

#--------------------
#pandas join, by default it will join the table left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

#Pandas inner join Dataframe
df3=df1.join(df2,lsuffix="_left",rsuffix="_right", how="inner")
print(df3)

#Pandas left join Dataframes
df3=df1.join(df2,lsuffix="_left",rsuffix="_right", how="left")
print(df3)


#Pandas Right join Dataframes
df3=df1.join(df2,lsuffix="_left",rsuffix="_right", how="right")
print(df3)

#Pandas join on Cloumns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
print(df3)

#Pandas left join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='left')
print(df3)


#Pandas Right join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='right')
print(df3)


#------------------------------------------------------------------
#pandas merge  Dataframes

import pandas as pd

technologies={
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30Days','40Days','35days','50Days'],
    
    }

index_lables1=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_lables1)
df1
technologies2={
    'Courses':["Spark","Java","Python","Go"],
    "Discount":[2000,2300,1200,2000]
    }
index_lables2=['r1','r6','r3','r5']

df2=pd.DataFrame(technologies2,index=index_lables2)
df2


#using pandas.merge (inner join)
df3=pd.merge(df1, df2)


#-------------------------------------------------------------------------------
#using pandas concat() to connect two dataframes
import pandas as pd

technologies={
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
   }
df=pd.DataFrame(technologies)
df

technologies2={
    'Courses':["Pandas","Hadoop","Hyperian","Java"],
    "Fee":[20000,23000,12000,20000]
    }
df1=pd.DataFrame(technologies2)
df1


data=[df,df1]

df2=pd.concat(data)
df2


#concatenate multile Dataframe using pandas.concat()

import pandas as pd


df=pd.DataFrame(
    {
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
   })
df


df1=pd.DataFrame({
    'Courses':["Pandas","Hadoop","Hyperian","Java"],
    "Fee":[20000,23000,12000,20000]
    })
df1


df2=pd.DataFrame(
    {'Duration':['30Days','40Days','35days','60Days','55Days'],
     'Discount':[1000,2000,3000,4000,5000]
     })

df2

#Appending multiple DataFrame
df3=pd.concat([df,df1,df2])
print(df3)

