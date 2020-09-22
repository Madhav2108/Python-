import MySQLdb  # Open database connection
from prettytable import PrettyTable
db = MySQLdb.connect("localhost","root", "1234","d")
# prepare a cursor object using cursor() method
cursor = db.cursor() # execute SQL query using execute() method.
#Create
#sql = "create table xx(name char(30),address char(30));"
#insert
#sql = "insert into xx values('RAvi','Ram NAgar');"
#insert
#name=input("Enter Name : ")
#address=input("Enter Address: ")
#sql = "insert into xx values('"+name+"','"+address+"');"
sql ="select * from xx"
cursor.execute(sql)
t = PrettyTable(['name','address'])
results = cursor.fetchall()
for name,address in results:
    t.add_row([name,address])
    print(name,"--",address)
print(t)
print(sql)
cursor.execute(sql)
db.commit()
db.close()
