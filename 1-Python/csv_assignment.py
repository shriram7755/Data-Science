# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:05:02 2023

@author: SHRI
"""

import pandas as pd
import numpy as np

df=pd.read_csv('c:/2-dataset/loan.csv')
df.dtypes

df.shape  #(39717, 111)
df.size   # 4408587 access all the files
df.columns
df.columns.values  #access all column as array
df.index  #RangeIndex(start=0, stop=39717, step=1) 
df.columns[2] #loan_amnt'
df.loc[0:1] #
df.describe
df['term']
df[['id','member_id']]
df.info #[39717 rows x 111 columns]>
df.astype(str)

#Changing data types of file
df.dtypes
df.astype(str)
df=df.astype({"id":float, "member_id":float})
print(df)

#Column operation file
df=df.drop(['member_id'],axis=1) #Remove member_id
df



df=df.drop(0) #Delet 0th index row
df

df=df.drop(df.index[2:1]) #Row 3 on wards are deleted
df
################################################################################
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


###############################################################################