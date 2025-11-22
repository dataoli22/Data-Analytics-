#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

# Establishing a connection
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="TEST"
)

# Creating a cursor object
cursor = cnx.cursor()

# Executing a query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetching the results
results = cursor.fetchall()

# Displaying the results
for row in results:
    print(row)

# Closing the cursor and connection
cursor.close()
cnx.close()


# In[2]:


import os
import pymysql
import pandas as pd

host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user="root",
    passwd=password,
    db="TEST",
    charset='utf8mb4')

df = pd.read_sql_query("SELECT * FROM YOUR_TABLE",
    conn)
df.tail(10)


# In[ ]:




