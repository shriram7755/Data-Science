# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:17:28 2023

@author: SHRI
"""

#-----------------------------                            Python For NLP                   -------------------------------------------------------------------

import re
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''

pattern ='\d\d\d\d\d\d\d\d\d\d'
maches=re.findall(pattern,text)
maches


#-------------------------------------------------------------------------------
#Another method
import re
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''

#pattern ='\(\d{3}\)-\d{3}-\d{4}'
pattern ='\(\d{3}\)-\d{3}-\d{4}|\d{10}'

maches=re.findall(pattern,text)
maches


#----------------------------------------------------------------------------------
'''
A protracted; legal battle; over a 32-carat;
 Golconda diamond-
 
 We want any character except  ;  and - pattern  will be[^;-]
 Goto to Regular expression and type we will get the text
 
 '''
 import re 
 text1='''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''
 
 
 pattern='[^;-]'
 maches=re.findall(pattern,text1)
 maches
 
 
 #-----------------------------------------------------------------------------
 #when you want only one line not next line [^\n] 
 #use + or *
 
import re
text3='''
Note 1 - Summary of Significant Accounting Policies Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
Reclassifications
Certain prior period balances have been reclassified to conform to the current period presentation in the accompanying notes.
Revenue Recognition
Revenue by source
The following table disaggregates our revenue by major source (in millions):
  '''
 
 
pattern='Note \d - [^\n]*'
maches=re.findall(pattern,text3)
maches

############################################################################################################################################
#------------------------------------------------------------------------------
import re
text3='''
Note 1 - Summary of Significant Accounting Policies Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
Reclassifications
Certain prior period balances have been reclassified to conform to the current period presentation in the accompanying notes.
Revenue Recognition
Revenue by source
The following table disaggregates our revenue by major source (in millions):
  '''
 
 
pattern='Note \d - ([^\n]*)'      #(........) capture everything enclosed
maches=re.findall(pattern,text3)
maches


#---------------------------------------------------------------------------------
#now let us take another text
#Extract finicial peroids from a company's finicial 

import re

text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q\d'
maches=re.findall(pattern, text)
maches

#-------------------------------------------------------------------------------
#Another method


import re

text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1234]'
maches=re.findall(pattern, text)
maches

#----------------------------------------------------------------------------------
#you can give  range
import re

text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1-4]'
maches=re.findall(pattern, text)
maches

#---------------------------------------------------------------------------------
#what if ypur text comprises of 
import re
text5='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1-4]'    
maches=re.findall(pattern, text5,re.IGNORECASE)
maches

# ['FY2021 Q1']

#--------------------------------------------------------------------------------
#want both uppercase and lowercase
import re
text5='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1-4] | fy\d{4} Q[1-4]'


matched=re.findall(pattern, text5)    #['FY2021 Q1 ', ' fy2020 Q4']
matched=re.findall(pattern, text5,re.IGNORECASE)  # [' FY2021 Q1', ' fy2020 Q4']
matched


#-------------------------------------------------------------------------------
#now let us assume we want only 2021 Q1 and 2020 Q4 , then 
#you can get extract through(.....)
import re
text5='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern='FY(\d{4} Q[1-4])'      #(........) capture everything enclosed
maches=re.findall(pattern, text5,re.IGNORECASE)

# ['2021 Q1', '2020 Q4']


--------------------------------------------------------------------------------
#Now let us assume that only finicial number

import re
text5='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern='\$[0-9\.]+'                #['$4.85', '$3']
matches=re.findall(pattern, text5)
matches

#------------------------------------------------------------------------------
#if we dont want $ just put (), after $
import re
text5='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern='\$([0-9\.]+)'                #['4.85', '3']
matches=re.findall(pattern, text5)
matches

#--------------------------------------------------------------------------------

