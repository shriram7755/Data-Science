#######################################################################################

#Dictionary
# a dictionary is a set of associations
# bet key and value that is unordered 
#changable(mutable) and indexed
#duplicates not allows in dictionary
#dict cannot have 2 items with same key


#creating Dictionary
capitals={
    'maharashtra':'mumbai',
    'Gujrat':'Ahmadbad',
    'UP':'Lakhnow',
    'karnataka':'Banglore',
    'Andrapradesh':'Hydrabad'
    
    }
print(capitals)   

#accessing Items via Keys

print('capitals[maharashtra]:', capitals['maharashtra'])

#adding new Entry

capitals['west_Bengal']='Kolkatta'
capitals

#Changing a key value

capitals['Gujrat']='Gandhinagar'
print(capitals)

#remove an entry
capitals.pop('karnataka')
print(capitals)

del capitals['UP']
print(capitals)

#iterating Over key
capitals={
    'maharashtra':'mumbai',
    'Gujrat':'Ahmadbad',
    'UP':'Lakhnow',
    'karnataka':'Banglore',
    'Andrapradesh':'Hydrabad'
    }

for states in capitals:
    print(states, end=", ")
    
for states in capitals:
    print(states, end=", ")
    print(capitals[states])

#values keys items


print(capitals.values())
print(capitals.keys())
print(capitals.items())

############333
#checking key menbership
capitals={
    'maharashtra':'mumbai',
    'Gujrat':'Ahmadbad',
    'UP':'Lakhnow',
    'karnataka':'Banglore',
    'Andrapradesh':'Hydrabad'
    }
print('karnataka' in capitals)
print('bihar' not in capitals)

#obtaining the length of dictionary
print(len(capitals))


#Dictionary can have values  in tuple

seasons = {'summer':('feb','mer','apr', 'may'),
           'Rainy':('june','july','aug','sep'),
           'winter':('oct','nov','dec','jan')}

print(seasons['Rainy'])
print(seasons['Rainy'][0])


#Dictionary Methods
#get() is a useful method to access the
#values of key in dictionary
#dict cannot have 2 items with same key
dict2={
       'brand':'Maruti',
       'model':'breeza',
       'year':2021,
       'year':2020
       }

print(dict2)


#Loop through a Dict, it will only show keys
dict2={
       'brand':'Maruti',
       'model':'breeza',
       'year':2021,
       'year':2020
       
       }


for x in dict2:
    print(x , end=" :")
    print(dict2[x])
    
for x in dict2:
    print(dict2[x])
    

############################################




