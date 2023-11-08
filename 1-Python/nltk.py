# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:59:36 2023

@author: SHRI
"""

#base or root form
#these mainly relay on chopping#stemming
#stemming is the process of reducing 
#inflected/drived words to their word stem,
#base or root form 
#these mainly rely of chopping-off 's', 'es', 'ed',
#'ing' 'ly' etc from the end of words
#and some times the conversion is not desirable
#But nonetheless, stemming helps us in standardizing text


import nltk #function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("we are eating and swimming ; we have been eating and swimming ; he eats and swims ; he ate and swam ")
# ing are removed in these sentences.

#through stemming and lemitation both generator the
 
import re
line ='asdf fjdk; afed, fjek,asdf,foo'

re.split(r'(?:,|;\s)\s*', line)
pattern=r'(?:,|;\s)\s*'
#--------------------------------------------------
x=re.split(pattern, txt)
print(x) 

#----------------------------------------------------------
filename='spam.txt'
filename.endswith('.txt')
#-------------------------------------------------------
area_name='6 th Lane west Andheri'
area_name.endswith('west Andheri')

#----------------------------------------------------

url=('http://www.python.org')

#----------------------------------------------
#Slicing of string
[start:stop:step]
#Data preprocessing

S='ABCDEFGHI'
print(S[2:7])

#slice with negative indexing
S='ABCDEFGHI'
print(S[-7:-2])

#slice with negative and positive indexing
S='ABCDEFGHI'
print(S[2:-5])   #CD

#specify the step of slicing
S='ABCDEFGHI'
print(S[2:7:2])   #CEG

#
S='ABCDEFGHI'
print(S[6:1:-2])   #GEC

#slicing with first three character from string
S='ABCDEFGHI'
print(S[6:])       #GHI


#Reversing the string
S='ABCDEFGHI'
print(S[::-1])   #IHGFEDCBA

#silimer operation can be done with slices
filename='spam.txt'
filename[-4:]=='.txt'

#check file extension
from fnmatch import fnmatch,fnmatchcase
names= ['Dat1.csv','Dat2.csv','config.ini','foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]

#-----------------------------------------------------
from fnmatch import fnmatch,fnmatchcase
names=['Andheri East','Parle East','Dabur West']
[name for name in names if fnmatch(name, '* East')]

#---------------------------------------------------------------

addresses=[
    '5412 N ClARK ST',
    '1060 W ADDISON ST',
    '!039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    
    ]
from fnmatch import fnmatch,fnmatchcase
[addres for addres in addresses if fnmatch(addres, '* ST')]


#----------------------------------------------------------------
#feature engineering
text='yeah,but no,but yeah,but no,but yeah'
#Extract match
text=='yeah'
#match the start or end
text.startswith('yeah')
text.endswith('no')

#search the location
text.find('no')


#---------------------------------------------------------------
text1='11/27/2012'
text2='Nov 27, 2012'

import re
#Simple matching: \+d means match one or digits
if re.match(r'(\d+/\d+/\d+)', text1):
    print('Yes')
else:
    print('No')

#Yes

import re
#Simple matching: \+d means match one or digits
if re.match(r'(\d+/\d+/\d+)', text2):
    print('Yes')
else:
    print('No')
#No

#--------------------------------------------------------------------
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat, text1):
    print("yes")
else:
    print("No")
#Yes

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat, text2):
    print("yes")
else:
    print("No")
#--------------------------------------------------------------------
#Searching and replacing text
text='yeah,but no,but yeah,but no,but yeah'
text.replace('yeah', 'yep')  

#------------------------------------------------------------------
#if you dates in format 11/27/2012 want to convert 2012-11-27
text ='Today is 11/27/2012. Pycon starts 3/13/2013'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# if you want to know how many substitution are 
#made in text  them
#you can use subn() method
newtext, n=datepat.subn(r'\3-\1-\2',text)
newtext
n

#-----------------------------------------------------------------
text='UPPER PYTHON, lower python, mixed Python' 
re.findall('python', text, flags=re.IGNORECASE)
#to substitute
re.sub('python','snake', text, flags=re.IGNORECASE)
#'UPPER snake, lower snake, mixed snake'

#-------------------------------------------------------------------
#The last example reveals a limitation that 
#replacing the text won't match the case of the
#matched text If you need to fix this,
#you might have to use a support function, as in the#following
import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.islower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace()

text3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE) #error
text3
        
#-------------------------------------------------------------------------
#pattern matching
str_pat=re.compile(r'\"(.*)\"')
text1='Computer says "no."'
str_pat.findall(text1)   #['no.']

#-------------------------------------------------------------------
#drawback
text2='Computer says "no." Phone says "yes."'
str_pat.findall(text2)
#str_pat.findall(text1)

#---------------------------------------------------------------------
#REMOVE DRAWBACK VIMP
str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
#['no.', 'yes.']

#--------------------------------------------------------------------
comment =re.compile(r'/\*(.*?)\*/')
text1='/*This is a comment */'
comment.findall(text1) #['This is a comment ']

#-------------------------------------------------------------------
text2='''/*This is a 
multiline comment */
'''
comment.findall(text2)
#
comment=re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)    error
#(?:.|\n) capture group

comment=re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)

#------------------------------------------------------------------
'''
VIMP encoding questions
types
1)ascii 
2)unicode 
3)UTF-8 (unicode transformation format)
$)UTF-32
What is encoding?
transformation of human lang to

'''
#normalizing Unicode text to standard Representation
s1='Spicy Jalape \u00f1o'
s2='Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
# False

#-------------------------------------------------------------------
import unicodedata
t1=unicodedata.normalize('NFC', s1)
t2=unicodedata.normalize('NFC', s2)
t1==t2        #error

#--------------------------------------------------------------------
#encoding is important in web scrapping

'''
unicode only define 1


'''
string1="apple"
string2="jeei125"
string3="12345"
string4="pre@12"

string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')


#------------------------------------------------------------------------
text='one 🐘 and three 🐋'
print(text)
print(len(text))

'''
we encode the string into a bytes type using the utf8 encoding
and print the bytes.
We count the number of bytes in the encoding type.
'''

e=text.encode('utf8')
print(e)
print(len(e))

e=text.encode('utf16')
print(e)
print(len(e))

#----------------------------------------------------------------------------
fname='data.txt'

with open(fname,  mode='rb') as f:
    contents=f.read()
    
    
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))


#------------------------------------------------------------------------------
fname='data.txt'

with open(fname,  mode='rb') as f:
    contents=f.read()
    
    
    print(type(contents))
    print(contents)
    print(contents.decode('utf16'))

#------------------------------------------------------------------------------
#Stripping inwanted characters from string

s='    hello world   \n'
s.strip()
#'hello world'

s='    hello world   \n'
s.lstrip()
#'hello world   \n'

s='    hello world   \n'
s.rstrip()
#'    hello world'

#character stripping
t='-------------hello============='
t.lstrip('-')
#'hello============='

t='-------------hello============='
t.strip('-=')
#'hello'


s='  hello world                 \n'
s=s.strip()
s
#'hello world'


s.replace(' ', '')
#'helloworld'


import re
re.sub('\s+',' ',s)
#'hello world'

#------------------------------------------------------------------------------
#aligning the text string

text='Hello World'
text.ljust(20)
#'Hello World         '

text='Hello World'
text.rjust(20)
#'         Hello World'

text='Hello World'
text.center(20)
text.rjust(20)
#text='Hello World'

#------------------------------------------------------------------------------

#All of these method accept an optional characters and fill

text.rjust(20,'=')#'=========Hello World'
text.center(20,'')#'****Hello World****'

#------------------------------------------------------------------------------
format(text, '>20')
#'         Hello World'

format(text, '<20')
#'Hello World         '

format(text, '^20')
'    Hello World     '

#------------------------------------------------------------------------------
#character
format(text,'=>20s')
#'=========Hello World'


format(text,'*^20s')
#'****Hello World*****'

#------------------------------------------------------------------------------
#These format codes can also be used in the format method
#value of the example

'{:>10s} {:>10s}'.format('Hello ', 'World')
#'    Hello       World'

#------------------------------------------------------------------------------
"""One benefits of the format ()is that is not specified 
to string making it more general purpose. 
For instance, you can use it
"""
x = 1.2345
format(x, '>10')
x

format(x, '^10.2f')
#------------------------------------------------------------------------------
parts=['Is','Chicago','Not','hicago']
' '.join(parts)
#'Is Chicago Not hicago'

#------------------------------------------------------------------------------
','.join(parts)
'Is,Chicago,Not,hicago'

#------------------------------------------------------------------------------
''.join(parts)
#'IsChicagoNothicago'

#------------------------------------------------------------------------------
