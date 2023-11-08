qq"""
Created on Thu Aug  3 16:05:02 2023

@author: SHRI
"""
#DataSet Operations assignment


import pandas as pd
df=pd.read_csv("c:/2-dataset/loan.csv")
df

#number of rows and columns
df.shape

#multiplication of rows and columns
df.size

#name of columns
df.columns    #Accces all column as index

#
df.columns.values      # Access all columns as Array


#start=0,stop=39717,step=1
df.index

#type of column
df.dtypes

#to take information
df.info

#accessing one column content
df['id']

#accessing two column contents
df[['id','loan_amnt']]

#accessing the all rows from 39000th row
df2=df[39000:]
df2
 
#accessing specific element
df['loan_amnt'][4]

#subtracting 500 from all the elements of loan_amnt
df['loan_amnt']=df['loan_amnt']-500
df['loan_amnt']

#it gives 5 numbers summary
df.describe()

#rename the column
df2=df.rename({'id':'name'},axis=1)

#rename the row
df2=df.rename({3:'03'},axis=0)

#drop rows by labels
df1=df.drop([5,7])

#delete rows by index
df1=df.drop(df.index[1])

#drop columns by name
df2=df.drop(['annual_inc'],axis=1)

#it extracts all rows and 0 to 1 columns
df2=df.iloc[:,0:2]

#selects rows from 0 to 1 and columns from 0 to 1
df2=df.iloc[0:2,0:2]

#all the rows with mentioned columns
df2=df.loc[:,["id",'loan_amnt','term']] 




############################################################



#number of rows and columns
df.shape

#multiplication of rows and columns
df.size

#name of columns
df.columns

#start=0,stop=45211,step=1
df.index

#type of column
df.dtypes

#it gives 5 numbers summary
df.describe()

#to take information
df.info

#accessing one column content
df['age']

#accessing two column contents
df[['age','loan']]

#accessing the all rows from starting to 4th row
df2=df[:5]
df2

#accessing specific element
df['age'][35]

#subtracting 5 from all the elements of balance
df['balance']=df['balance']-5
df['balance']

#rename the column
df2=df.rename({'duration':'period'},axis=1)

#rename the row
df2=df.rename({3:'03'},axis=0)

#drop rows by labels
df1=df.drop([5,7])

#delete rows by index
df1=df.drop(df.index[1])

#drop columns by name
df2=df.drop(['previous'],axis=1)

#it extracts all rows and 0 to 1 columns
df2=df.iloc[:,0:2]

#selects rows from 0 to 1 and columns from 0 to 1
df2=df.iloc[0:2,0:2]

#all the rows with mentioned columns
df2=df.loc[:,["age",'loan','default']] 



##########################################################


import pandas as pd
df=pd.read_csv("c:/2-dataset/crime_data.csv")
df

#number of rows and columns
df.shape

#multiplication of rows and columns
df.size

#name of columns
df.columns

#start=0,stop=49,step=1
df.index
`
#type of column
df.dtypes

#it gives 5 numbers summary
df.describe()

#to take information
df.info

#accessing one column content
df['Murder']

#accessing two column contents
df[['Murder','Rape']]

#accessing the all rows from starting to 4th row
df2=df[:5]
df2

#accessing specific element
df['Rape'][35]

#subtracting 5 from all the elements of balance
df['Assault']=df['Assault']-10
df['Assault']

#rename the column
df2=df.rename({'Unnamed:0':'Name'},axis=1)

#rename the row
df2=df.rename({3:'03'},axis=0)

#drop rows by labels
df1=df.drop([5,7])

#delete rows by index
df1=df.drop(df.index[1])

#drop columns by name
df2=df.drop(['UrbanPop'],axis=1)

#it extracts all rows and 0 to 1 columns
df2=df.iloc[:,0:2]

#selects rows from 0 to 1 and columns from 0 to 1
df2=df.iloc[0:2,0:2]

##########################################################
