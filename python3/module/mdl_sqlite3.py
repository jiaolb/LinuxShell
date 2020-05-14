#!bin/usr/python
# -.- coding:UTF-8 -.-

import sqlite3

#建立并连接数据库
conn = sqlite3.connect('C:/Users/Administrator/Desktop/test.db')
print ("Opened database successfully")

c = conn.cursor()

#删表操作
try:
	print ("Table created successfully")
	c.execute("DROP TABLE COMPANY")
except:
    print ("Delete database, but table is not exist")

#建表操作
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully")

#插入数据
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
print ("Table insert successfully")

#SELECT 操作
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0], end = '  ')
   print ("NAME = ", row[1], end = '  ')
   print ("ADDRESS = ", row[2], end = '  ')
   print ("SALARY = ", row[3])
print ("Table select successfully")

#UPDATE操作
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0], end = '  ')
   print ("NAME = ", row[1], end = '  ')
   print ("ADDRESS = ", row[2], end = '  ')
   print ("SALARY = ", row[3])
print ("Table update successfully")

#删除操作
c.execute("DELETE from COMPANY where ID=2;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0], end = '  ')
   print ("NAME = ", row[1], end = '  ')
   print ("ADDRESS = ", row[2], end = '  ')
   print ("SALARY = ", row[3])
   
conn.commit()
conn.close()






