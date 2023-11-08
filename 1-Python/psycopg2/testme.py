# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:21:49 2023

@author: SHRI
"""

import psycopg2 as pg2

#create a conncetion with PostgreSQl
# 'password' is whatever password you set , we set password



conn=pg2.connect(database='TESTME', user='postgres', password='root')

cur =conn.cursor()


#Execute a Command: create a courses table
cur.execute('''CREATE TABLE courses1(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) UNIQUE NOT NULL,
    course_instructor  VARCHAR(100)  NOT NULL,
    topic  VARCHAR(20) NOT NULL);
''')



conn.commit()


cur.close()
