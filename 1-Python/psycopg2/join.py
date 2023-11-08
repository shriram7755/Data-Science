# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:23:35 2023

@author: SHRI
"""

import psycopg2 as pg2


conn=pg2.connect(database='TESTME',user='postgres', password='root')

cur= conn.cursor()


conn.commit()

cur.execute('''SELECT course_name,course_instructor,topic,course_duration,course_fees
            FROM courses1
            INNER JOIN Programming_language
            ON courses1.courses_id=Programming_language.courses_id''')

rows=cur.fetchall()

