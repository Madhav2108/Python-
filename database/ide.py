import MySQLdb
from prettytable import PrettyTable
db = MySQLdb.connect("localhost","root","1234","d")
cursor = db.cursor()
#insert
name  = input("Enter student Name : ")
address = input("Enter address: ")
sql = "insert into x values ('"+name+"','"+address+"');"
print(sql)
cursor.execute(sql)
db.commit()
#display
sql ="select * from x"
cursor.execute(sql)
t = PrettyTable(['name','address'])
results = cursor.fetchall()
for name,address in results:
    t.add_row([name,address])
print(t)
#delete
#read rec
sql ="select * from x"
cursor.execute(sql)
t = PrettyTable(['name','address'])
results = cursor.fetchall()
for name,address in results:
    t.add_row([name,address])
print(t)
#select field value
data = input("Enter Name :")
sql =  "delete from x where name ='"+data+"'"
cursor.execute(sql)
db.commit()
#resulet after delete
sql ="select * from x"
cursor.execute(sql)
t = PrettyTable(['name','address'])
results = cursor.fetchall()
for name,address in results:
    t.add_row([name,address])
print(t)
#update
name = input("Enter Name :")
address = input("Enter Address :")
sql =  "update x set address= '"+address+"' where name ='"+name+"'"
cursor.execute(sql)
db.commit()

