 O# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:18:05 2023

@author: SHRI 
"""

#--------------------          MATPLOTLIB ------------------------------>
#important in visulization 

# in matplotlib select all code and then run 

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()

#-----------------------------------------------
#Multiline plot
import matplotlib.pyplot as plt
x=range(1,5)

plt.plot(x, [xi*1.5 for xi in x])

plt.plot(x, [xi*3.0 for xi in x])

plt.plot(x, [xi/3.0 for xi in x])
 
plt.show()

#-----------------------------------------------

#Note how matplotlib automatically
#choose different colours

#Grid axis and labal 

import matplotlib.pyplot as plt
import  numpy as np

x= np.arange(1,5)
plt.plot(x, x*1.5,x, x*3.0, x,x/3.0) #x-is used for x -axis
plt.grid(True)
plt.show()

#--------------------------------------------------
#Handling axes
import matplotlib.pyplot as plt
import  numpy as np

x= np.arange(1,5)
plt.plot(x, x*1.5,x, x*3.0, x,x/3.0)

plt.axis()

plt.axis([0,5,-1,13]) #set new axes limit
#[xmin,xmax,ymin,ymax]
#[0,5,-1,13]
plt.show()

#-----------------------------------------------------
#addling lables
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.xlabel("This is X axis: ")

plt.ylabel("This is Y axis: ")

plt.show()

#-----------------------------------------------------
#Matplotlib provide the simple function, plt.title()
#adding title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.title('Simple plot')

plt.show()

#-----------------------------------------------------
#Adding a leagend
import matplotlib.pyplot as plt
import  numpy as np

x= np.arange(1,5)
plt.plot(x, x*1.5,label='Normal')

plt.plot(x, x*3,label='Fast')

plt.plot(x, x/3,label='Slow')

plt.legend()

plt.show()

#--------------------------------------------------------
'''Colour Abbrivation
Color          Name
b              blue
c              cyan
g              green
k              black
m              magenta
r              red
w             white
y              yellow
'''
#-------------------------------------------------------------
#Control Colors
import matplotlib.pyplot as plt
import  numpy as np

y=np.arange(1, 3)
plt.plot(y, 'y');
plt.plot(y+1, 'm');
plt.plot(y+2, 'c');
plt.show()


#---------------------------------------------------------
#specifying style in multiline plots
import matplotlib.pyplot as plt
import  numpy as np

y=np.arange(1, 3)
plt.plot(y, 'y',y+1,'m',y+2,'c');
plt.show()
#control line style
import matplotlib.pyplot as plt
import  numpy as np

y=np.arange(1, 3)
plt.plot(y, '--',y+1,'-.',y+2,':');
plt.show()

#------------------------------------------------------------
'''style abbrivation style
-solid line
--dashed line
-. dash dot line
: dotted line

#Control marker style

'''
import matplotlib.pyplot as plt
import  numpy as np

y=np.arange(1, 3, 0.2)

plt.plot(y, 'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s');
plt.show()

#-------------------------------------------------------------
#Histogram chart
import matplotlib.pyplot as plt
import  numpy as np
y=np.random.randn(1000)
plt.hist(y)                #IMP Commond 
plt.show() 


#----------------------------------------------------------------
#bar plot
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
plt.show()

#------------------------------------------------------------
#scatter plot
import matplotlib.pyplot as plt
import  numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()


#-------------------------------------------------------------

size = 50*np.random.randn(1000)
colours =np.random.randn(1000)
plt.scatter(x ,y, s=size, c=colours)
plt.show()

#--------------------------------------------------------------
#adding text
import matplotlib.pyplot as plt
import  numpy as np
X=np.linspace(-4, 4,1024)
Y= .25 * (X+4.) * (X+1.)*(X-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(X,Y,c='k')
plt.show()

 

--------------------------------- SEABORN LIBRARY -----------------------
#How to use seaborn for Data visualizaion

import seaborn as sns
import pandas 
import matplotlib.pyplot as plt
#Seaborn has 18 in-bulid datasets,
#that can found using the following command
sns.get_dataset_names()
df=sns.load_dataset('titanic')  #vi internet
df.head()

#Count Plot
'''
A count plot is helpful when dealing with categorical value
it is used to plot the frequency of different category.
The columns sex contains categorial data in the title data .
i.e male and female.


'''
sns.countplot(x='sex',data=df)
#x- The name of the colums
#Data- The dataframe
sns.countplot(x='sex',hue='survived' ,data=df, palette='Set1')

sns.countplot(x='sex',hue='survived' ,data=df, palette='Set2')

sns.countplot(x='sex',hue='survived' ,data=df, palette='Set3')

#hue = The name of the catorical columns to split the bars

#palette -The color palette to be used .



#------------------------------------------------------------------
#KDE plot
#A kernal density Estimation plot is used
# to plot the distribution of continuous data.

sns.kdeplot(x='age',data=df, color='black')
#x- The name of the colums
#Data- The dataframe
# X- the name of colums , You can find list of column


#Distrubution plot
sns.displot(x='age',kde=True ,bins=6 ,data=df)

  #kde -It is set to false by default.
  #bins - the number of bins/bars.
  
sns.displot(x='age',kde=True,bins=5,
hue=df['survived'],palette='Set1', data=df)

#First , we will need to load the iris dataset.
df=sns.load_dataset('iris')
df.head()

#scatter the plot help understand co-relation between data,
import seaborn as sns
import pandas 
import matplotlib.pyplot as plt
sns.scatterplot(x='sepal_Length',y='petal_length',data=df,hue='species')
#error

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')


'''
kind - the kind of the plot 
It can be one of the following.

'scatter','hist','hex','kde','reg','resid'

''' 

#pair plots
sns.pairplot(df)

#A head map can be used to visualize confusion , matrices
#,and correlation
corr=df.corr()
sns.heatmap(corr)

