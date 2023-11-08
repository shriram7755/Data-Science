# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:32:51 2023

@author: SHRI
"""
import pandas as pd

path='c:/2-dataset/Seeds_data.csv'
df=pd.read_csv(path)
df

#info
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 210 entries, 0 to 209
Data columns (total 8 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   Area             210 non-null    float64
 1   Perimeter        210 non-null    float64
 2   Compactness      210 non-null    float64
 3   length           210 non-null    float64
 4   Width            210 non-null    float64
 5   Assymetry_coeff  210 non-null    float64
 6   len_ker_grove    210 non-null    float64
 7   Type             210 non-null    int64  
dtypes: float64(7), int64(1)
memory usage: 13.3 KB
None '''
#-----------------------------------------------------------------------------------
df.describe()

#access first three row
 print("First three row of the dataframe : ")
 print(df.iloc[:3])
'''
    Area  Perimeter   Compactness  ...  Assymetry_coeff  len_ker_grove  Type
0  15.26       14.84       0.8710  ...            2.221          5.220     1
1  14.88       14.57       0.8811  ...            1.018          4.956     1
2  14.29       14.09       0.9050  ...            2.699          4.825     1

[3 rows x 8 columns]
'''
#----------------------------------------------------------------------------------\
# print("select the 'Area' and 'width' Columns from Dataframe: ")
 print(df[['Area','Width']])
'''
      Area  Width
0    15.26  3.312
1    14.88  3.333
2    14.29  3.337
3    13.84  3.379
4    16.14  3.562
..     ...    ...
205  12.19  2.981
206  11.23  2.795
207  13.20  3.232
208  11.84  2.836
209  12.30  2.974

[210 rows x 2 columns]
'''
#----------------------------------------------------------------------------------
#print(" select the specific column and rows : ")
print(df[['Area','Compactness']])
'''
      Area  Width
0    15.26  3.312
1    14.88  3.333
2    14.29  3.337
3    13.84  3.379
4    16.14  3.562
..     ...    ...
205  12.19  2.981
206  11.23  2.795
207  13.20  3.232
208  11.84  2.836
209  12.30  2.974

[210 rows x 2 columns]
'''
#-------------------------------------------------------------------------------------
#print("Select all rows where area is greater than 14 ")
print(df[df['Area']>14])

'''
      Area  Perimeter   Compactness  ...  Assymetry_coeff  len_ker_grove  Type
0    15.26       14.84       0.8710  ...            2.221          5.220     1
1    14.88       14.57       0.8811  ...            1.018          4.956     1
2    14.29       14.09       0.9050  ...            2.699          4.825     1
4    16.14       14.99       0.9034  ...            1.355          5.175     1
5    14.38       14.21       0.8951  ...            2.462          4.956     1
..     ...         ...          ...  ...              ...            ...   ...
135  15.38       14.66       0.8990  ...            3.600          5.439     2
136  17.36       15.76       0.8785  ...            3.526          5.971     2
137  15.57       15.15       0.8527  ...            2.640          5.879     2
138  15.60       15.11       0.8580  ...            2.725          5.752     2
139  16.23       15.18       0.8850  ...            3.769          5.922     2

[116 rows x 8 columns]
'''

#---------------------------------------------------------------------------------
##find total rows
total_rows=len(df.axes[0])
total_rows
#210


#print("find all row the Area is between 15 to 20 : ")
df2=(df[df['Area'].between(15,20)])
print(df2)

'''
      Area  Perimeter   Compactness  ...  Assymetry_coeff  len_ker_grove  Type
0    15.26       14.84       0.8710  ...            2.221          5.220     1
4    16.14       14.99       0.9034  ...            1.355          5.175     1
8    16.63       15.46       0.8747  ...            2.040          5.877     1
9    16.44       15.25       0.8880  ...            1.969          5.533     1
10   15.26       14.85       0.8696  ...            4.543          5.314     1
..     ...         ...          ...  ...              ...            ...   ...
135  15.38       14.66       0.8990  ...            3.600          5.439     2
136  17.36       15.76       0.8785  ...            3.526          5.971     2
137  15.57       15.15       0.8527  ...            2.640          5.879     2
138  15.60       15.11       0.8580  ...            2.725          5.752     2
139  16.23       15.18       0.8850  ...            3.769          5.922     2

[81 rows x 8 columns]
'''


# display tha 'Area' is less than 13 and 'Type' is greater than  1
df2=(df[(df['Area']<13) & (df['Type']>1)])
print(df2)
'''
      Area  Perimeter   Compactness  ...  Assymetry_coeff  len_ker_grove  Type
143  12.22       13.32       0.8652  ...            5.469          5.221     3
144  11.82       13.40       0.8274  ...            4.471          5.178     3
145  11.21       13.13       0.8167  ...            6.169          5.275     3
146  11.43       13.13       0.8335  ...            2.221          5.132     3
147  12.49       13.46       0.8658  ...            4.421          5.002     3
..     ...         ...          ...  ...              ...            ...   ...
204  12.37       13.47       0.8567  ...            3.919          5.001     3
205  12.19       13.20       0.8783  ...            3.631          4.870     3
206  11.23       12.88       0.8511  ...            4.325          5.003     3
208  11.84       13.21       0.8521  ...            3.598          5.044     3
209  12.30       13.34       0.8684  ...            5.637          5.063     3

[65 rows x 8 columns]
'''

#calculate sum of of Area column
print(df['Area'].sum())                          #3117.98
print(df['length'].sum()                         #1181.9920000000002


# mean of Area Columns
print(df['Area'].mean())                         #14.84752380952381


# append new Row in dataframe to gives values of each columns
df.loc['k']=['25', '15','0.80','6.02','3.12','2','4','2']
print(df)
'''
0    15.26      14.84       0.871  ...           2.221          5.22    1
1    14.88      14.57      0.8811  ...           1.018         4.956    1
2    14.29      14.09       0.905  ...           2.699         4.825    1
3    13.84      13.94      0.8955  ...           2.259         4.805    1
4    16.14      14.99      0.9034  ...           1.355         5.175    1
..     ...        ...         ...  ...             ...           ...  ...
206  11.23      12.88      0.8511  ...           4.325         5.003    3
207   13.2      13.66      0.8883  ...           8.315         5.056    3
208  11.84      13.21      0.8521  ...           3.598         5.044    3
209   12.3      13.34      0.8684  ...           5.637         5.063    3
k       25         15        0.80  ...               2             4    2

[211 rows x 8 columns]
'''

#Ascending and Desending
df =df.sort_values(by=['Area'] , ascending=[False]) # Decending 
print(df)
'''
      Area  Perimeter   Compactness  ...  Assymetry_coeff  len_ker_grove  Type
88   21.18       17.21       0.8989  ...            5.780          6.231     2
114  20.97       17.25       0.8859  ...            4.677          6.316     2
89   20.88       17.05       0.9031  ...            5.016          6.321     2
77   20.71       17.23       0.8763  ...            4.451          6.451     2
120  20.24       16.91       0.8897  ...            5.901          6.188     2
..     ...         ...          ...  ...              ...            ...   ...
193  10.82       12.83       0.8256  ...            4.853          5.089     3
175  10.80       12.57       0.8590  ...            4.773          5.063     3
149  10.79       12.93       0.8107  ...            5.462          5.194     3
177  10.74       12.73       0.8329  ...            4.702          4.963     3
189  10.59       12.41       0.8648  ...            4.975          4.794     3

[210 rows x 8 columns]
'''

df =df.sort_values(by=['Type'] , ascending=[True])
print(df)
'''
      Area  Perimeter   Compactness  ...  Assymetry_coeff  len_ker_grove  Type
68   14.37       14.39       0.8726  ...            1.464          5.300     1
51   15.78       14.91       0.8923  ...            5.593          5.136     1
56   14.46       14.35       0.8818  ...            2.802          5.044     1
52   14.49       14.61       0.8538  ...            4.116          5.396     1
54   14.52       14.60       0.8557  ...            1.481          5.487     1
..     ...         ...          ...  ...              ...            ...   ...
204  12.37       13.47       0.8567  ...            3.919          5.001     3
200  12.38       13.44       0.8609  ...            5.472          5.045     3
166  12.44       13.59       0.8462  ...            4.924          5.270     3
208  11.84       13.21       0.8521  ...            3.598          5.044     3
189  10.59       12.41       0.8648  ...            4.975          4.794     3

[210 rows x 8 columns]
'''


#iterate over rows in a Dataframe

for index,row in df.iterrows():
    print(row['Area'],  row['Type'])
'''
14.37 1.0
15.78 1.0
14.46 1.0
14.49 1.0
14.43 1.0
14.29 1.0
14.33 1.0
13.99 1.0
13.94 1.0
13.89 1.0
13.84 1.0
13.8 1.0
13.78 1.0
15.69 1.0
15.38 2.0
15.56 2.0
15.57 2.0
15.6 2.0
15.38 2.0
'''

#Accessing one column contents []
df['Area']
'''
0      15.26
1      14.88
2      14.29
3      13.84
4      16.14
 
205    12.19
206    11.23
207    13.20
208    11.84
209    12.30
'''

#Accessing two column contents [[]]
df[['Area','Width']]
'''
      Area  Width
0    15.26  3.312
1    14.88  3.333
2    14.29  3.337
3    13.84  3.379
4    16.14  3.562
..     ...    ...
205  12.19  2.981
206  11.23  2.795
207  13.20  3.232
208  11.84  2.836
209  12.30  2.974

[210 rows x 2 columns]
'''



# Convert Data type to all  column in a list  #IMP in Interview
df.dtypes
'''
Area               float64
Perimeter          float64
Compactness        float64
length             float64
Width              float64
Assymetry_coeff    float64
len_ker_grove      float64
Type                 int64
dtype: object
'''
cols=["Area","Width"]
df[cols]=df[cols].astype('int')
df.dtypes
'''
Area                 int32
Perimeter          float64
Compactness        float64
length             float64
Width                int32
Assymetry_coeff    float64
len_ker_grove      float64
Type                 int64
dtype: object
'''



# Rename a Single Column 
df2=df.rename(columns = {'Area':'Area_A'})
print(df2.columns)
'''
Index(['Area_A', 'Perimeter ', 'Compactness', 'length', 'Width',
       'Assymetry_coeff', 'len_ker_grove', 'Type'],
      dtype='object')
'''

#drop two or more columns 
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
'''
0         0.8710   5.763      3            2.221          5.220     1
1         0.8811   5.554      3            1.018          4.956     1
2         0.9050   5.291      3            2.699          4.825     1
3         0.8955   5.324      3            2.259          4.805     1
4         0.9034   5.658      3            1.355          5.175     1
..           ...     ...    ...              ...            ...   ...
205       0.8783   5.137      2            3.631          4.870     3
206       0.8511   5.140      2            4.325          5.003     3
207       0.8883   5.236      3            8.315          5.056     3
208       0.8521   5.175      2            3.598          5.044     3
209       0.8684   5.243      2            5.637          5.063     3

[210 rows x 6 columns]
'''



#-----------------------------------------------------------------
some other operation
df.dtypes # its show the types of the columns i.e float64,int64 
df.shape  #(210, 8) 210 <--rows , 8<--- columns
df.size   #1680   no_of_rows*no_of_columns 
df.columns  # all colums name and its dtype 
df.columns.values
df.index            #RangeIndex(start=0, stop=210, step=1)
df.columns[2]       #'Compactness'
df.loc[0:1]         # 0 to 1 all rows (1 includes)
