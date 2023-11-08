# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:58:54 2023

@author: SHRI
"""

import pandas as pd

path='c:/2-dataset/Iris.csv'
df=pd.read_csv(path)
df

#-----------------
#apply mathematical operation(Add)  to specific columns 
def add_3(x):
    return x+3


df2=((df.SepalLengthCm).apply(add_3))
df2

'''
0      12.1
1      11.9
2      11.7
3      11.6
4      12.0

145    13.7
146    13.3
147    13.5
148    13.2
149    12.9
Name: SepalLengthCm, Length: 150, dtype: float64
'''
#--------------------
#when you are apply both the Columns then you need to pass list of columns 
def add_4(x):
    return x+4
df[['SepalLengthCm','SepalWidthCm']]=df[['SepalLengthCm','SepalWidthCm']].apply(add_4)
df
'''
      Id  SepalLengthCm  ...  PetalWidthCm         Species
0      1            9.1  ...           0.2     Iris-setosa
1      2            8.9  ...           0.2     Iris-setosa
2      3            8.7  ...           0.2     Iris-setosa
3      4            8.6  ...           0.2     Iris-setosa
4      5            9.0  ...           0.2     Iris-setosa
..   ...            ...  ...           ...             ...
145  146           10.7  ...           2.3  Iris-virginica
146  147           10.3  ...           1.9  Iris-virginica
147  148           10.5  ...           2.0  Iris-virginica
148  149           10.2  ...           2.3  Iris-virginica
149  150            9.9  ...           1.8  Iris-virginica

[150 rows x 6 columns]
'''

#-----------------
#lambda function to Specific  columns 
df2=df['SepalLengthCm']=df['SepalLengthCm'].apply(lambda x:x +10)
df2
'''
0      19.1
1      18.9
2      18.7
3      18.6
4      19.0

145    20.7
146    20.3
147    20.5
148    20.2
149    19.9
Name: SepalLengthCm, Length: 150, dtype: float64
'''

#-----------------
#lambda function to Specific  columns 
#transform
df2=df['SepalLengthCm']=df['SepalLengthCm'].transform(lambda x:x +10)
df2
'''
0      15.1
1      14.9
2      14.7
3      14.6
4      15.0

145    16.7
146    16.3
147    16.5
148    16.2
149    15.9
Name: SepalLengthCm, Length: 150, dtype: float64
'''

#-----------------
#USing pandas.Dataframe.map() to single Column

df['SepalLengthCm']=df['SepalLengthCm'].map(lambda SepalLengthCm:SepalLengthCm/2.)
df
'''
      Id  SepalLengthCm  ...  PetalWidthCm         Species
0      1           2.55  ...           0.2     Iris-setosa
1      2           2.45  ...           0.2     Iris-setosa
2      3           2.35  ...           0.2     Iris-setosa
3      4           2.30  ...           0.2     Iris-setosa
4      5           2.50  ...           0.2     Iris-setosa
..   ...            ...  ...           ...             ...
145  146           3.35  ...           2.3  Iris-virginica
146  147           3.15  ...           1.9  Iris-virginica
147  148           3.25  ...           2.0  Iris-virginica
148  149           3.10  ...           2.3  Iris-virginica
149  150           2.95  ...           1.8  Iris-virginica

[150 rows x 6 columns]
'''

#----------------------
##square of a column
df['SepalLengthCm']=df['SepalLengthCm'].apply(np.square)
print(df)
'''
      Id  SepalLengthCm  ...  PetalWidthCm         Species
0      1          26.01  ...           0.2     Iris-setosa
1      2          24.01  ...           0.2     Iris-setosa
2      3          22.09  ...           0.2     Iris-setosa
3      4          21.16  ...           0.2     Iris-setosa
4      5          25.00  ...           0.2     Iris-setosa
..   ...            ...  ...           ...             ...
145  146          44.89  ...           2.3  Iris-virginica
146  147          39.69  ...           1.9  Iris-virginica
147  148          42.25  ...           2.0  Iris-virginica
148  149          38.44  ...           2.3  Iris-virginica
149  150          34.81  ...           1.8  Iris-virginica

[150 rows x 6 columns]
'''


#

#----------------
#Using list(df) to get the columns headers as a list
column_headers=list(df.columns)
column_headers
'''
['Id',
 'SepalLengthCm',
 'SepalWidthCm',
 'PetalLengthCm',
 'PetalWidthCm',
 'Species']
'''


#---------------
#Pandas suffle Dataframe ROWS
#Suffle the dataframe rows &return all rows

df1=df.sample(frac=1)
print(df1)
'''
      Id  SepalLengthCm  ...  PetalWidthCm          Species
141  142            6.9  ...           2.3   Iris-virginica
104  105            6.5  ...           2.2   Iris-virginica
26    27            5.0  ...           0.4      Iris-setosa
76    77            6.8  ...           1.4  Iris-versicolor
102  103            7.1  ...           2.1   Iris-virginica
..   ...            ...  ...           ...              ...
70    71            5.9  ...           1.8  Iris-versicolor
45    46            4.8  ...           0.3      Iris-setosa
113  114            5.7  ...           2.0   Iris-virginica
58    59            6.6  ...           1.3  Iris-versicolor
6      7            4.6  ...           0.3      Iris-setosa
'''

#--------------
#info
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             150 non-null    int64  
 1   SepalLengthCm  150 non-null    float64
 2   SepalWidthCm   150 non-null    float64
 3   PetalLengthCm  150 non-null    float64
 4   PetalWidthCm   150 non-null    float64
 5   Species        150 non-null    object 
dtypes: float64(4), int64(1), object(1)
memory usage: 7.2+ KB
None
'''
#df.describe()
df.describe()
'''
               Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count  150.000000     150.000000    150.000000     150.000000    150.000000
mean    75.500000       5.843333      3.054000       3.758667      1.198667
std     43.445368       0.828066      0.433594       1.764420      0.763161
min      1.000000       4.300000      2.000000       1.000000      0.100000
25%     38.250000       5.100000      2.800000       1.600000      0.300000
50%     75.500000       5.800000      3.000000       4.350000      1.300000
75%    112.750000       6.400000      3.300000       5.100000      1.800000
max    150.000000       7.900000      4.400000       6.900000      2.500000
'''

#access first three row
 print("First three row of the dataframe : ")
 print(df.iloc[:3])
'''
   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            1.3           0.2  Iris-setosa
'''

#returns rows*columns
df.size

#returns column names
df.columns.values

#gives information of dataframe
df.describe()

#gives (rows,columns)
df.shape

#gives column names
df.columns

#gives information of dataframe
df.info

#start end end of index
df.index

#data type of dataframe
df.dtypes

#to convert all in string
df1=df.convert_dtypes()
df1.dtypes

#convert datatype in object
df=df.astype(str)
df.dtypes

#rename the column
df2=df.rename({'Id':'Id_Number'},axis=1)

#to acess single column
df['Id']

#access two columns
df[['Id','Species']]

#drop rows by labels
df1=df.drop([5,7])


#selects rows from 0 to 1 and columns from 0 to 1
df2=df.iloc[0:2,0:2]

#selects below rows only
df1=df.loc[:,["Id",'Species','SepalLengthCm']]

#Quick example of get the number of rows in DataFrame
rows_count=len(df.index)
rows_count
 
rows_count=len(df.axes[0])
rows_count

#to get number of columns in dataframe
columns_count=len(df.axes[1])
columns_count

#query all rows with Id equal to 10
df3=df.query("Id == 10")
print(df3)

#Not equal condition 
df2=df.query("Id ! = 10")
print(df2)

#adding new row in dataframe
df.loc['150']=[151,4.2,7.8,3.9,2.6,'Iris-setosa']

print("First three row of the dataframe : ")
print(df.iloc[:3])

print(" select the specific column and rows : ")
print(df[['Id','Species']])

print(" Id's in the data is greater than 2: ")
print(df[df['Id']>2])

df2=df.loc[df.Id>2]
df2

print("row the Id is between 15 to 20 : ")
df2=(df[df['Id'].between(15,20)])

print("no of Id in the data is less than 2 and Id is greater than 15 : ")
df2=(df[(df['Id']>2) & (df['Id']<15)])
print(df2)

print("\n Change the value in row '7' to 11.5 :")
df.loc[7, 'SepalLengthCm'] = 11.5  
print(df)

print("sum of the SepalLengthCm  in data: ")
print(df['SepalLengthCm'].sum())

print("\nto calculate the mean of all PetalLengthCm:  ")
print(df['PetalLengthCm'].mean())

df =df.sort_values(by=['SepalLengthCm'] , ascending=[True])
print(df)
df =df.sort_values(by=['PetalLengthCm'] , ascending=[False])
print(df)
print("sort the dataframe first by 'SepalLengthCm' in ascending order ,then by 'PetalLengthCm' in desecending order")
print(df)

#apply function to all columns
#in all elements 3 gets added
def add(x):
    return x+3
df2=df.apply(add) 
df2

df2=df['Id'].apply(add)
df2



