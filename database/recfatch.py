import MySQLdb
from prettytable import PrettyTable
db = MySQLdb.connect("localhost","root","","d" )
cur = db.cursor()
"""cur.execute('create table x1 (name char(20),roll int)')
cur.execute('insert into x1 values("Amit",12)')
cur.execute('insert into x1 values("Sumit",14)')
cur.execute('insert into x1 values("Ravi",15)')
cur.execute('insert into x1 values("Raman",14)')"""
cur.execute('insert into x1 values("Amit",12)')
cur.execute('insert into x1 values("Sumit",14)')
cur.execute('insert into x1 values("Ravi",15)')
cur.execute('insert into x1 values("Raman",14)')
cur.commit()
p=cur.execute("select count(*) from x1")
print(p)
"""results = cur.fetchall()
t = PrettyTable(['Name','Roll'])
for name,roll in results:
    t.add_row([name,roll])
    # print(name,roll)
print(t)"""
