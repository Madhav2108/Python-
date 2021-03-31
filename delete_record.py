
import MySQLdb
db = MySQLdb.connect("localhost","root","","cable")
cursor = db.cursor()
name = input("Enter any name : ")
sql ="delete from customer where name like '%" + name + "';"
cursor.execute(sql)
db.commit()
db.close()
print("Row deleted successfully")
