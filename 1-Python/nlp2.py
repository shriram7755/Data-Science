# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:24:46 2023

@author: SHRI
"""
#Tokenization
:Defination : The process of spliting sentences into constitients words.
Tyeps: 
    Unigram - Hello , sanjivani , Ai
    Bigram  - two 
    trigram  -three words

POS - part of speech (POS) tagging 
lemitization - in a paragraph in sentence has one words and these words are appers in below sentence 
this words has synonyms words are appers in below line.

Certain group of multiple words are treated as one entity e.g USA United state of america
Multiwords expression tokonization.


white space tokennization
 


name entity Recognization:
there are some words in sentences that are not in dictionary 

    
text='Welcome to the new year 2023'
x=text.split()
print(x)

#------------------------------------------------------------------------------
#import 
import re #function remove the special character '@' '
def remove_special_characters(text):
    #define pattern to keep
    pattern= r'[^a-zA-Z0-9.,!?/:;\"\'\s]'
    #except a-z,A-Z,0-9,
    return re.sub(pattern, '', text)

#call function
remove_special_characters("007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $550USD!")


#---------------------------------------------------------------------------------
#removing numbers

import re #function remove the special character
def remove_numbers(text):
    #define pattern to keep
    pattern= r'[^a-zA-Z.,!?/:;\"\'\s]'
    #except a-z,A-Z,0-9,
    return re.sub(pattern, '', text)

#call function
remove_numbers("007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $550USD!")

#-----------------------------------------------------------------------------------------
#not sure if this was fun! What to do you think  of it.?USD 
import re
text='Welcome: to the, new year; 2023!'
x=re.split(r'(?:,|;|\s)\s*',text)
print(x)

#--------------------------------------------------------------------------------------
#Removing punctuations marks
'''
This can be clubbed with stepmof removing
sppecial characters. Removing panctuation is fairly easy.
it can be achived by using string.punctuation and keeping everything 
which is not in the list
'''

import string #function remove punctuation
def remove_punctuation(text):
    text = ''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('Article: @First sentence of some, {important} article having lot of ~ punctutaions. Amd another one;!')
 


#stemming
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
