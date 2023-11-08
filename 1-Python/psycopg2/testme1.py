# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:23:36 2023

@author: SHRI
"""

import psycopg2 as pg2

#CREATE a connection with  postgreSQL
# 'Password' is whatever password you set we set in the install 

conn=pg2.connect(database='TESTME',user='postgres', password='root')

#Establish a conncetion and start curser to be ready to query
cur=conn.cursor()


cur.execute('''INSERT INTO courses1(course_name,course_instructor,topic)
           VALUES('Introducing to SQL' ,'Ram' ,'JUlia') ''');
           
cur.execute('''INSERT INTO courses1
           (course_name,course_instructor,topic)
           VALUES('Analysing Survay Data in Python' ,'Sham' ,'Python') ''');
           
cur.execute('''INSERT INTO courses1
           (course_name,course_instructor,topic)
           VALUES('Introducing to Chatgpt' ,'Ganesh' ,'Theory') ''');
           
           
cur.execute('''INSERT INTO courses1
           (course_name,course_instructor,topic)
           VALUES('Introducing to Statistics in R' ,'Ramesh' ,'R') ''');
           
cur.execute('''INSERT INTO courses1
           (course_name,course_instructor,topic)
           VALUES('Hypothesis Testing in Python' ,'Jayesh' ,'Python') ''');
           
conn.commit()

cur.close()

conn.close()
