# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:03:04 2023

@author: SHRI
"""

import psycopg2 as pg2

conn=pg2.connect(database='TESTME',user='postgres', password='root')

cur=conn.cursor()

cur.execute('SELECT course_instructor, COUNT(*) FROM courses1 GROUP BY course_instructor')

conn.commit()


rows=cur.fetchall()

for row in rows:
    print(row)