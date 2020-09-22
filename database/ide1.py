import MySQLdb
from prettytable import PrettyTable
db = MySQLdb.connect("localhost","root","1234","d")
cursor = db.cursor()
#display Normal
sql = "SELECT * FROM x ;"
print("Name , Address")
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name = row[0]
        address= row[1]
        print (name,",",address)
except:
    print ("Error: unable to fecth data")

#display in  table using PrettyTable
    
sql ="select * from x"
cursor.execute(sql)
t = PrettyTable(['name','address'])
results = cursor.fetchall()
for name,address in results:
    t.add_row([name,address])
print(t)
db.close()
