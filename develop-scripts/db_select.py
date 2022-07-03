# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:28:40 2022
@author: azizcanhamas
"""

import sqlite3 as sql

db=sql.connect("citizens_db.sqlite")
cursor=db.cursor()
res=cursor.execute("SELECT * from citizens WHERE first_name='JOHN' AND last_name='WICK' AND registration_city='NEW YORK'")
value=res.fetchall()
for i in value:
    for x in i:
        print(x)
    print("================")
db.close()