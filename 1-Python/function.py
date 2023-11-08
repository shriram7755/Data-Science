def prime_num(num):
    for i in range (2,num):
        if(num%i==0):
           return "The number is not prime"
        break
    
    return "the number is prime"

print(prime_num(11))

#------------------------------------------------------------------------------
#function without argument
def greet_user():
#"""Display a simple greeting."""
    print("Hello!")
    
greet_user()

#------------------------------------------------------------------------------
#passing info to a function 
def greet_user(username):
#"""Display a simple greeting."""
    print(f"Hello,{username}!")
    
greet_user("Sanjivani AI")

#------------------------------------------------------------------------------
#Argument and Parameter

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('Dog' , 'Moti')

#------------------------------------------------------------------------------

#Q create a program  using math and fstring tells us how many days ,
#weeks and months we are left if we willl leave until 80 years.
def crt(current_age, life_expectancy=80):
    if current_age >= life_expectancy:
        return "Congratulations! You have already exceeded the expected age."

    years_left = life_expectancy - current_age
    days_left = years_left * 365
    weeks_left = years_left * 52
    months_left = years_left * 12

    return f"You have approximately {days_left:,} days, {weeks_left:,} weeks, and {months_left:,} months left until you reach 80 years of age."

a=int(input("Enter age: "))
crt(a)

#------------------------------------------------------------------------------

#Q write program for roller poster  if height is 
#Q if your age is under 18 yrs then ticket will be 20 rs , 
#if greater than 18 yrs then ticket will be 50 rs , if age less than 12 & height is 120cm ticket 10 rs
#12 -18 age & height is 120cm ticket 15


def roller_cooster(height,age):  
    if height==18 :
        print('ticket is 20rs')
    elif age>18 and height==120 :
        print('ticket is 50rs')
    elif age<12 and height==120 :
       print('ticket is 10rs')
    elif 12<age>18 and height==120:
        print('ticket is 15rs')
        
a=int(input("Enter age: "))
b=int(input("Enter height: "))

roller_cooster(a,b)

#------------------------------------------------------------------------------
#Returning a Dictionary

def build_person(first_name,last_name):
#Return a dictionary of information about a person
    person ={"first":first_name, 'last':last_name}
    return person
musician=build_person('ram','Sarkar')
print(musician)




#------------------------------------------------------------------------------

#Passing a list

def greet_users(names):
    #print a simple greeting to each user in the list
    for name in names:
        msg=f"Hello, {name.title()}!"
        print(msg)
username =['sanket' , 'saurabh', 'Surabhi']
greet_users(username)

#------------------------------------------------------------------------------
#passing an arbitrary Number of Arguments
def make_pizza(*toppings):
    #print the list of topping that have been requested
    print(toppings)
make_pizza('pipperoni')
make_pizza('mushrooms' , 'green peppers', 'extra cheese')



#-------------------------------------------------------------------------------
#now we can replace the print() call with  loop that run through
#the list of topping and describe the pizza being ordered:
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pipperoni')
make_pizza('mushrooms' , 'green peppers', 'extra cheese')

#------------------------------------------------------------------------------

#Mixing Positional and arbitrary Arguments

def make_pizza(size,*toppings):
    #summarize the pizza we are about to make
    print(f"\n Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom', 'green peppers', 'extra cheese')


#------------------------------------------------------------------------------
#importing our module 
#import pizza module in function


import pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushroom', 'green peppers', 'extra cheese')

#_-----------------------------------------------------------------------------
#importing a specific function

from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom', 'green peppers', 'extra cheese')


#------------------------------------------------------------------------------
#Using as to give a FinctionS an Alias
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushroom', 'green peppers', 'extra cheese')


#------------------------------------------------------------------------------
#Using as to give  a  module as Alis
import pizza as p 
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom', 'green peppers', 'extra cheese')


#------------------------------------------------------------------------------
#importing all function in module
from pizza import *
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom', 'green peppers', 'extra cheese')

#------------------------------------------------------------------------------
#scope of variable 
x=x+1
x=6
print(x)

#You cannot initilise the value of variable before extecutiing it further operation

#first initialise varible 
#------------------------------------------------------------------------------
x=6
x=x+1
print(x)

#------------------------------------------------------------------------------
#lamda function
#A lambda function is a small anonymous function.
def add(a,b,c):
    sum=a+b+c
    #print(sum)
    return 
#add(4,5,6)
print(add(4,5,6))

#------------------------------------------------------------------------------
#name of function= lambda argument : business logic
#lamda function
#A lambda function is a small anonymous function.
add=lambda a,b,c:a+b+c
add(4,5,6)


#------------------------------------------------------------------------------

def mul(a,b,c):
    multi=a*b*c
    return multi
print(mul(6,7,8))

mul=lambda a,b,c:a*b*c
mul(6,7,8)

#------------------------------------------------------------------------------
val=lambda *args:sum(args) # args used for more variable for sum multiple
val(1,2,3,5,6)
val(1,2,3,5,7,8,9)

#------------------------------------------------------------------------------
#*args
def person(name,**data):
    print(name)
    print(data)

person(name='navin' ,age=28, place='mumbai' , mob_no=985060)



#------------------------------------------------------------------------------

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person(name='navin' ,age=28, place='mumbai' , mob_no=985060)

#------------------------------------------------------------------------------
#lambda function

val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)

#------------------------------------------------------------------------------

max=lambda a,b: a if(a>b)
print(max(1,2))  #error


max=lambda a,b: a if(a>b) else b
print(max(3,1))
print(max(8,10))

