

import pandas as pd
import numpy as np
df=pd.read_csv('c:/2-dataset/bank_data.csv')
df

df.dtypes
df.size
df['age']
df[['age','balance']]
#convert all types to best possible types

df2=df.convert_dtypes()
print(df2.dtypes)

###change types for one or multiple columns
df=df.astype({"age":float,"loan":float})
print(df.dtypes)

#convert data types for all columns in a list
cols=['age','balance']
df[cols]=df[cols].astype('int')
df.dtypes

## Substracting specific values from a cloumn
df['age']=df['age']-5 
df['age']

#it shows 5 number summery
df.describe

#rename() specific column 
df.rename(columns = {"loan": "loan_bal"},  inplace = True)
df
#renaming multiple columns
df.rename({"age": "ages", 
           "balance": "balance's", 
           "pdays": "paydays"}, 
          axis = "columns", inplace = True)
df
df.info

#select rows by index list
df2=df.iloc[[2,3,6]]

#select rows by integer index
df2=df.iloc[1:5]
df2
#select first rows
df2=df.iloc[:1]
df2
#select first 3 rows
df2=df.iloc[:3]
df2
#select last rows
df2=df.iloc[-1:]

#select last 3 rows
df2=df.iloc[-3:]

#select alternate rows
df2=df.iloc[::2]



df=pd.read_csv('c:/2-dataset/crime_data.csv')
df.dtypes
df.shape  
df.size
df.columns
df.columns.values
df.index
df.columns[2]
df.loc[0:1]



 
###############################################################################
df=pd.read_csv('c:/2-dataset/bank_data.csv')
df.dtypes
df.shape  
df.size
df.columns
df.columns.values
df.index
df.columns[2]
df.loc[0:1]

