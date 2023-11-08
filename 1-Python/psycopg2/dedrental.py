# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:36:55 2023

@author: SHRI
"""

import psycopg2 as pg2

#CREATE a connection with  postgreSQL
# 'Password' is whatever password you set we set in the install 
conn = pg2.connect(database='dedrental',user='postgres',password='root')

#Establish a conncetion and start curser to be ready to query
cur =conn.cursor()

#pass in a PostgreSQL Query as a string
cur.execute("SELECT * FROM payment")

#return a tuple of first row as Python objects
cur.fetchone()

#Return N Number of rows
cur.fetchmany(10)

#Return all rows at once
cur.fetchall()

# TO Save and index results , assign it to a variable

data= cur.fetchmany(10)




#Don't Forget close the connection
#killing the kernal or shutting  down  ju

conn.close()
