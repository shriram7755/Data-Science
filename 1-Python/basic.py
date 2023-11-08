
print("Hello World!")

#variable
'''
Types of Numbers
3 types:
    integers
    floting point
    complex number
'''

x=1
print(x)
print(type(x))
x=10000000000000000000000000000000000000000000000000001
print(x)
print(type(x))




age1=input("Please enter your age: ")
print(type(age1))

print(age1)

age2=input("Please enter your age: ")
print(type(age2))
age=age1+age2
print(age)

age1=int(input("Please enter your age: "))
print(type(age1))
print(age1)

age2=int(input("Please enter your age: "))
print(type(age2))
age=age1+age2
print(age)

#floating points numbers

exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))

#converting to flaot
#as with integers it is possible to convert other
#type such as an int or a  string into flaot

int_value=100
string_value='1.5'
float_value=float(int_value)
print('int value as flaot :' ,float_value)
print(type(float_value))
float_value=float(string_value)
print("string value as float: ",float_value)
print(type(float_value))


#complex number
c1=1 
c2=2j  
print('c1:', c1, ',c2:', c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)



#boolean value
#python support another type called Boolean
#a Boolean type can only of True or False
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))


#convert string into boolean
status = bool(input('OK it is confirmed?: '))
print(status)
print(type(status))



#arithmetaic  operators
#if you are adding two int no the result will be int 
#if you are adding flaot int float the result will be float 
home =10
away =15
print(home + away)
print(type(home + away))
print(10*4)
print(type(10*4))
goals_for=10 
goals_against =7
print(goals_for - goals_against)
print(type(goals_for - goals_against))


#if you are dividing two int no the result will be float

print(100/20)
print(type(100 /20))

print(100//20)
print(type(100 //20))

#modulo  operator

print("Modulo division 100%13 :" ,100%13)
print("Modulo division 3 % 2 :" ,3 % 2)

#power operation 
a=5
b=3
print(a**b)

#assignment Operators

+= compound opeartor

x=0
x+=1  
print(x)
# has behaviour as x=x+1
#####
#None Value

#boolean 
#is and is not are used for boolean operation
#is winner==None
#is not winner!=none

winner =None
print(winner is None)
#alternatevly you can write also:
print(winner is not None)


winner = None
print('winner: ',winner)
print('winner is None: ',winner is None)
print('winner is not None:',winner is not None)
print(type(winner))
print('set winner to True')
winner =True
################################################

#flow control using If Statements
#for loop

num=int(input('Enter a number: '))
if num>0:
    print(num)
    
#else if statement
num=int(input('Enter yet another number: '))
if num<0:
    print('Its Negative')
else:
    print('Its not negative')
    
#elif condition

saving=float(input("Enter how much you are in saving: "))
if saving==0:
    print("Sorry no Saving ")
elif saving<500:
    print("well done")
elif saving<1000:
    print("Thats a tidy sum")
elif saving <10000:
    print("Welcone Sir!")
    
#while loop

count =1
print("Starting")
while count<=10:
    print(count)
    count+=1

#for loop
#loop[ over a set of value in a range]
whenever you are using range function the range will be n-1 



#break
print("Only print code if all iteration is completed")
num = int(input('Enter a number to check :'))
for i in range(0,16):
    if i==num:
        break
    print(i)
print('done')
    

#now we use 'anonymous' loop variable
for _ in range(0,10):   #imp in interview
    print('.' , end='')
    print()
    
for _ in range(0,10):
    print('.' , end='') 
    
#break loop statements
print("Only print code if all iteration is completed")    
num = int(input('Enter a number to check :'))
for i in range(0,60):
    if i==num:
        break
    print(i,' ', end='')
print('done')

#location of print is changed
print("Only print code if all iteration is completed")    
num = int(input('Enter a number to check :'))
for i in range(0,6):
    if i==num:
        break
    print(i,' ', end='')
    print('done')

#print odd no in a given range

start,end =4,19

#interrating in no in list

for num in range(start,end+1):
    
    #checking condition
    if num%2!=0:
        print(num, end=" ")


#print even no in a given range

start,end =4,19

#interrating in no in list

for num in range(start,end+1):
    
    #checking condition
    if num%2==0:
        print(num, end=" ")
        
# print all even no in a range ,range(start,end,step)
for Even_no in  range(0,15,2):
    print(Even_no , end='  ')
    
# print all odd no in a range
for odd_no in  range(1,15,2):
    print(odd_no , end='  ')
    
    
#take input from user print Even no

num1=int(input("Enter Start of range: "))
num2=int(input('Enter End of a range: '))

for i in range(num1,num2+1):
    if i%2==0:
        print(i , end=' ')
        
#take input from user print ODD no

num1=int(input("Enter Start of range: "))
num2=int(input('Enter End of a range: '))

for i in range(num1,num2+1):
    if i%2!=0:
        print(i , end=' ')
        
#prime number in a given range

num1 = int(input("Enter start  range :" ))
num2 = int(input("Enter End Range : "))

print("Prime numbers between", num1, "and", num2, "are:")

for num in range(num1, num2 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
#leap year
year=int(input("Enter year: "))
if  year%4==0 and year!=100  and year%400==0:
    print("Enter year is leap year", year)
else:
    print("Enter year is not a leap year")


#check wheather a given string is palindrome or not
s=input("Enter String:  ")
strrev=(s[::-1])

if strrev==s:
    print("Palindrome")
else:
    print("Not palindrome")
  
#  # pattern      
for i in range(4):
    for j in range(4):
        print("#", end="  ")
    print()
    
for i in range(4):
    for j in range(i+1):
        print("#", end="  ")
    print()
    

for i in range(4):
    for j in range(4-i):
        print("#", end="  ")
    print()
    
    
#prime no 
num=int(input("Enter no :  "))
def prime_num(num):
    for i in range (2,num):
        if(num%i==0):
            return "The number is not prime "
            break
    return "number is prime "

#global variable
x="awesome"
def my_function():
    print("Python is "+x)
my_function()

# global and local variable
#local variable access only a block of code 
x="awesome"
def my_function():
    x="fantastic"
    print("Python is "+x)
my_function()

#dictionary
x={"name":"ram" , "age":34}
print(type(x)) 

###
str1="hello"
str2=2 
str3=str1+str2
#here will be error:can only concatenate str(not "int") to str
#string
#if you want multiple string use """
x="""This is python.
it is very powerful"""
print(x)


#string slicing 
#its start from a range and end with n-1

x="This is python .It is very powerful"
print(x)

#Ex
x="This is python .It is very powerful"
print(x[2:8])

#slice from the start
print(x[:3])

#slice from the end
print(x[4:])

#negative indexing
print(x[-5:-2])

#modify string
print(x.upper())


print(x.lower())

#remove whitespace 
print(x.strip())

x="Hello , World"
print(x.replace("Hello", "Gello"))

#use of split which replace white space/or ,
x="Hello , World"
print(x.split(","))

x="Hello  World"
print(x.split(" "))

#################333
x="Hello World"
string1=x[::-1]
print(string1)

###########
x="This is python and It is very powerful"
print(x.find("and"))


#string concatenates
x="Hello"
y="world"
print(x+y)
print()
print(x+" "+y)

#string format

x=36
y="my name is Anthomy"

#print(x+y)
#it will give error
print(f"my name is Anthony and my age is {x}")


###
quantity=3
item_no=54
price=67
print(f" I want {quantity} pieces and item number is{item_no}, its price is {price}")

my_order="I want {} pieces and item number is{}, its price is {}"
print(my_order.format(quantity,item_no,price))

my_order="I want {0} pieces and item number is{1}, its price is {2}"
print(my_order.format(quantity,item_no,price))

#escape character allow you to use double quotes when you normally world(escape character)
text="This is fun fair and its has got big \"round rigo\""
print(text)

############
a=10
b=20
print(a!=b)

print(3*3+3/3-3)

#Rule for mathematical operation
PEMDAS
p:parenthesis
E:Expoential
M:multiplication
D:divison
A:Addition
S:Substraction


print("Welcome to roller coaster ")
height=int(input("please  enter a height in a cm : "))
bill=0

if height>=120:
    print("You are elligible for roller coaster ")
    age=int(input("Please enter your age: "))
    if age<12:
        print("Child Ticket are $5")
        bill=5
    elif age<=18:
        print("youth ticket are 7$")
        bill=7
    else:
        print("Adult ticket are $12")
        bill=12
    want_photo=input("Do you want photo Y OR N")
    if want_photo=='Y' or 'y':
        bill=3
        print(f"your total bill will be {bill}")
    else:
        print(f"your total bill {bill}")

else:
    print("Sorry you need to grow taller")
    
    
    
    
################################333



users=["admin" ,"employee" , "manager", "worker","staff"]

for user in users:
    if user=="admin":
        print("hello admin, would you like to see status report?")
    elif user=="employee":
        print("Hello Employee")
    elif user=="manager":
        print("Hello manager")
    elif user=="worker":
        print("Hello worker")
    else:
        print("hello")
        
        
        
##password picker###
#picks  the adjectives
adjectives = ['sleepy' , 'slow ' ,'smeelly',
             'wet' , 'fat' , 'red',
             'orange' , 'yellow', 'green',
             'blue', 'purple' , 'fluffy',
             'white', 'proud' , 'brave']

#picks  the nouns
nouns = ['apple' , 'dinosour', 'ball',
         'toaster' , 'goat' , 'dragon',
         'hammer', 'duck', 'panda']

#pick the words

import random
import string

adjective=random.choice(adjectives)
noun=random.choice(nouns)

#select a number

number=random.randrange(0,100)

#select a special character

special_char= random.choice(string.punctuation)

#create a new secure password

password = adjective + noun + str(number) + special_char
print("your new password is : %s " % password)


#
import random
import string
print("Welcome to password  picker!")
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    special_char= random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("your new password is : %s " % password)
    response = input('Would you like generate another password? Type y or n:')
    if response=='n':
        break
    
    
########################################
"""write python code that determine wheather  a password . we define  strong 
password if it follows 
following conditions
1.it must at least 8 characters
2.it must at least one upper case latter
3. it must at least one lower case letter

"""


def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    
#checks each characters in the password  and see  which 
#requirements meets
    for ch in  password:
        if ch>='A' and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>='0' and ch <="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
password=input("Enter password")
checkPassword(password)


p=input("Enter Password : ")
if checkPassword(p):
    print("Strong password")
else:
    print("Weak password") 
    
    
    
##############################################
print("What is your age")
years_today=input("years: ")
month_today=input("months :")
days_today=input(" days: ")

total_days_today=int(years_today)*365 +int(month_today)*30 + int(days_today)
print(f"your total age todays in days  {total_days_today}")
print("Let us assume you are expected to live 90 years")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live -total_days_today
print(f"Your remaining life in days  {remaining_days_to_live=}")


##############################################

print("Welcome to pizza hut ")
def bill():
    s=15
    m=20
    l=25
    
    ec=2
    ps=2
    pml=3   
    
    a=input("Enter the size of the pizza: 's', 'm' , 'l' ")    if a=='s':
        print("Your bill will be 15 Dollar!")
        b=input("you want pepproni Enter y or n:")
        if b=='y' or b=='Y':
            print("Your bill will be",s+ps)
        c=input("You want extra cheese? enter y or n") 
        if c=='y':
            print("your bill will be ",s+ps+ec)
            
    elif a=='m':
        print("Your bill will be 20 Dollar!")
        b=input("you want pepproni Enter y or n:")
        if b=='y' or b=='Y':
            print("Your bill will be",m+pml)
        c=input("You want extra cheese? enter y or n")  
        if c=='y':
            print("your bill will be ",m+pml+ec)
        
    elif a=='l':
        print("Your bill will be 25 Dollar!")
        b=input("you want pepproni Enter y or n:")
        if b=='y' or b=='Y':
            print("Your bill will be",l+pml)
        c=input("You want extra cheese? enter y or n") 
        if c=='y':
            print("your bill will be ",l+pml+ec)

bill()

    
txt = "We are the so-called  from the north."
print(txt.upper())


