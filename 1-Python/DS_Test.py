# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:09:32 2023

@author: SHRI
"""

#1)


    

def empty_list(input_list):
    if len(input_list) == 0:
        return True
    else:
        return False
    



    
#2)
original_list = [1, 2, 3, 4, 5]

squared_list = [x ** 2 for x in original_list]

print(squared_list)




#3)
dict = {'a':'Sakshi','b':'Sanket','c':'Mayuri'}
print('x' in dict)


#4)

dict = {i:i/100 for i in range(100,170,10)}
dict


#5)
import pandas as pd

data = {
    'course': ['Mathematics', 'History', 'Physics', 'Chemistry' ],
    'fee': [1000, 1500, 1200, 800],
    'duration': [3, 4, 3, 2],
    'tutor':[1,2,3,4]
}

df = pd.DataFrame(data)

print(df)



#6)
# Write the DataFrame to a CSV file
df.to_csv('data.csv')





#7)

def calculate_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum
    
# Example 
data = [10, 20, 30, 40, 50]
max_val, min_val = calculate_max_min(data)
print("Maximum:", max_val)
print("Minimum:", min_val)


#8)

multiply = lambda a, b: a * b

# Example 
result = multiply(5, 7)
print(result)



#9)

import numpy as np

# Create a NumPy array
array = np.array([0, 2, 0, 4, 0])
result = np.any(array != 0)

#10)

import matplotlib.pyplot as plt
X = [1,2,4,5]
Y = [4,8,5,7]
plt.plot(X,Y,'o',color = 'red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('lines plot')
plt.show()



#11)
import matplotlib.pyplot as plt
import pandas as pd
dict1 = {'Programming_lang':['Java','Python','PHP'],
        'Popularity':[22.2,23.7,8.8]}
df=pd.DataFrame(dict1)
plt.bar(df['Programming_lang'],df['Popularity'])
plt.show()




def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
    




