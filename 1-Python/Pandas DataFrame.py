# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:26:35 2023

@author: mobin
"""

#######################################################
#Pandas Dataframe
"""
It is a two-dimensional data structure, 
an immutable, heterogenous tabular 
data structure with labeled axes(rows and columns).

"""
##########################################################
#To check the version of pandas

import pandas as pd
pd.__version__

#########################################################
#Create using constructor
#Create pandas Dataframe from list

import pandas as pd
technologies = [["Spark",20000, "30days"],
                ["pandas",20000, "40days"]
                ]
df=pd.DataFrame(technologies)
print(df)
#######################################################
"""
Since we have not given labels to columns and indexes, 
DataFrame by default assigns incremental sequence 
numbers as lables to both rows and columns, these are 
called Index.
Add Column & Row labels to the DataFrame
"""

import pandas as pd
technologies = [["Spark",20000, "30days"],
                ["pandas",20000, "40days"]
                ]
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

#########################################################
#To check Datatypes(imp,hl,qrp)
df.dtypes
##########################################

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

#Convert Data type for all columns in a list

df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee','Discount']
df[cols] = df[cols].astype('float')
df.dtypes

#Ignores error

df = df.astype({"Courses": int},errors='ignore')
df.dtypes
 
#Generate error

df = df.astype({"Courses": int},errors='raise')
df.dtypes

#########################################
#Create DataFrame from DIctionary
import pandas as pd
technologies= {
    'Courses' :["Spark","Pyspark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration' :['30days','40days','50days'],
    'Discount' :[1000,2000,3000]
    }
df=pd.DataFrame(technologies)
df

#Convert datafram to csv
df.to_csv('technologies.csv')


#Convert datafram to csv
df=pd.read_csv('technologies.csv')
df
















 




















