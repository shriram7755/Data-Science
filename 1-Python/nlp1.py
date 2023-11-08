# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:34:11 2023

@author: SHRI
"""
#Go to anaconda navigator -->base -->open terminal -->pip install PyPDF2

from PyPDF2 import PdfFileMerger
#importing required module
from PyPDF2 import PdfReader

#creating a pdf reader object

reader=PdfReader('c:/1-Python/python_tutorial.pdf')

#print the number of pages in the file
print(len(reader.pages))

#getting a specific page from the pdf file
page=reader.pages[10]


#extracting text from page
text = page.extract_text()
print(text)

#---------------------------------------------------------------------------

import re
chat2 = 'Hi: I have a problem with my order number 412889912'
pattern = 'order [^\d]*(\d*)'
matches = re.findall(pattern,chat2)
matches                                        #['412889912']


import re
chat2 = 'Hi: I have a problem with my order number 412889912'
pattern = 'order* ([^\d]+\d*)'
matches = re.findall(pattern,chat2)
matches                                           #['number 412889912']


import re
chat2 = 'Hi: I have a problem with my order number 412889912'
pattern = 'order* [^\d]+\d*'
matches = re.findall(pattern,chat2)
matches                                           #['order number 412889912']


#------------------------------------------------------------------------------

import re
chat2 = 'Hi: I have a problem with my order number # 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern,chat2)
matches                                         #['412889912']

#------------------------------------------------------------------------------
import re
chat3 = 'Hi: My order 412889912 is having an issue, I was charger 300$ when online'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern,chat3)
matches
                                               #['412889912']

#------------------------------------------------------------------------------
def get_pattern_match(pattern,text):
    matches= re.findall(pattern, text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)', chat2)
                                                   #'412889912'

#extracting email from user
##Retrieve email id and phone
import re

chat1 = 'Hi: you ask lot of questions 1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'Hi: phone: 1235678912, email: abc@xyz.com'

#pattern = r'[A-Za-z0-9_]*@[a-z]*\.[a-z]{3}'

matches=re.findall(pattern,chat1)
matches

       #pattern writing  time give 'r' to avoid encoding error
       import re
       text='''
       Born	Elon Reeve Musk
       June 28, 1971 (age 52)
       Pretoria, Transvaal, South Africa
       Education	University of Pennsylvania (BA, BS)
       Title	
       Founder, CEO, and chief engineer of SpaceX
       CEO and product architect of Tesla, Inc.
       Owner and CTO of Twitter
       President of the Musk Foundation
       Founder of the Boring Company, X Corp., and xAI
       Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
       Spouses	
       Justine Wilson
       ​
       ​(m. 2000; div. 2008)​
       Talulah Riley
       ​
       ​(m. 2010; div. 2012)​
       ​
       ​(m. 2013; div. 2016)​
       Partner	Grimes (2018–2021)[1]
       Children	10[2]
       Parents	
       Errol Musk
       Maye Musk
       Family	Musk family
       '''
       def get_pattern_match(pattern,text):
           matches= re.findall(pattern, text)
           if matches:
               return matches[0]
           
       get_pattern_match(r'age (\d+)', text)
       get_pattern_match(r'Born(.*)\n', text).strip()
       get_pattern_match(r'Born. *\n(.*)\(age', text).strip()
       get_pattern_match(r'age. *\n(.*)', text)


       #-----------------------------------------------------------------------
       import re
       text ='''
       Born	Mukesh Dhirubhai Ambani
       19 April 1957 (age 66)
       Aden, Colony of Aden
       (present-day Yemen)[1][2]
       Nationality	Indian
       Alma mater	
       St. Xavier's College, Mumbai
       Institute of Chemical Technology (B.E.)
       Occupation(s)	Chairman and MD, Reliance Industries
       Spouse	Nita Ambani ​(m. 1985)​[3]
       Children	3
       Parents	
       Dhirubhai Ambani (father)
       Kokilaben Ambani (mother)
       Relatives	Anil Ambani (brother)
       Tina Ambani (sister-in-law)
       '''

       def get_pattern_match(pattern,text):
           matches= re.findall(pattern, text)
           if matches:
               return matches[0]
           
       def extract_personal_information(text):
           age=get_pattern_match('age (\d{2})', text)
           full_name = get_pattern_match('Born(.*)\n', text)
           birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
           birth_place= get_pattern_match('\(age.*\n(.*)', text)
           return {
               'age' : int(age),
               'name':full_name.strip(),
               'birth_date':birth_date.strip(),
               'birth_place':birth_place.strip()
               
               }

       extract_personal_information(text)

       #------------------------------------------------------------------                                          