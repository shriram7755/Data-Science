# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:48:15 2023

@author: SHRI
"""

import psycopg2 as pg2


conn=pg2.connect(database='TESTME',user='postgres', password='root')

cur= conn.cursor()

cur.execute('SELECT * FROM courses1;')

rows=cur.fetchall()

conn.commit()

conn.close()

for row in rows:
    print(row)
    