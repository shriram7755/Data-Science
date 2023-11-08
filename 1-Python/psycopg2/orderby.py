# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:09:39 2023

@author: SHRI
"""

import psycopg2 as pg2

conn=pg2.connect(database='TESTME',user='postgres', password='root')

cur=conn.cursor()

cur.execute('SELECT * FROM courses1 ORDER BY course_instructor')

conn.commit()


rows=cur.fetchall()

for row in rows:
    print(row)
    
    