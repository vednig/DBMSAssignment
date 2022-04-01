from turtle import color
import datetime

import mysql.connector
from faker import Faker

fake = Faker()
for _ in range(10):
  print(fake.name())

mydb = mysql.connector.connect(

  host="localhost",

  user="root",

  password="",
  db="Assignment"

)
tablename="sailors"
print(mydb)


cur = mydb.cursor()
create_table="Create Table SAILORS (SID int NOT NULL AUTO_INCREMENT PRIMARY KEY,SNAME varchar(45),RATING int,AGE int);"
cur.execute(create_table)
for i in range(1,10):
  SID=i
  SNAME=fake.name()
  RATING=fake.numerify(text="#")
  AGE=str(fake.numerify(text="##"))
  query="INSERT INTO "+tablename+" VALUES ("+str(SID)+',"'+SNAME+'",'+ str(RATING) +","+str(AGE)+");"
  print(query)
  cur.execute(query)
  print(cur.fetchall())
#for firstname, lastname in cur.fetchall() :
#    print( firstname, lastname )

tablename="boats"
print(mydb)


cur = mydb.cursor()
create_table="Create Table BOATS (BID int NOT NULL AUTO_INCREMENT PRIMARY KEY,BNAME varchar(45),COLOR varchar(26));"
cur.execute(create_table)
for i in range(1,10):
  BID=i
  BNAME=fake.name()
  COLOR=fake.color_name()
  print(COLOR)
  query="INSERT INTO "+tablename+" VALUES ("+str(BID)+',"'+BNAME+'","'+ COLOR +'");'
  print(query)
  cur.execute(query)
  print(cur.fetchall())
#for firstname, lastname in cur.fetchall() :
#    print( firstname, lastname )


tablename="RESERVES"
print(mydb)


cur = mydb.cursor()
create_table="Create Table RESERVES (SID int NOT NULL AUTO_INCREMENT PRIMARY KEY,BID int,Day date);"
cur.execute(create_table)

for i in range(1,10):
  SID=i
  BID=10-i
 # COLOR=fake.color()
  DATE=fake.date(pattern='%Y-%m-%d', end_datetime=datetime.date(1995, 1,1))
  query="INSERT INTO "+tablename+" VALUES ("+str(BID)+','+str(SID)+',"'+ DATE +'");'
  print(query)
  cur.execute(query)
  print(cur.fetchall())
#for firstname, lastname in cur.fetchall() :
#    print( firstname, lastname )


