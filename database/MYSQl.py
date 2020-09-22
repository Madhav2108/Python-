#pip install mysqlclient
import MySQLdb

def main():
    
    # Defining and manipulating database

    # Establish database connection
    conn = MySQLdb.connect("localhost","root","","workshop")
    print('Database Connected Successfully!!')
    
    # Create a cursor
    cur = conn.cursor()

    # Create a table
    cur.execute('CREATE TABLE STUDENT\
        (RollNum INT,\
         Name VARCHAR(20),\
         Percentage INT);')
    print('Table Created Successfully!!')
    
    # Inserting data into table
    cur.execute("INSERT INTO STUDENT VALUES (1, 'Hiten', 89);")
    cur.execute("INSERT INTO STUDENT VALUES (2, 'Muskan', 85);")
    cur.execute("INSERT INTO STUDENT VALUES (3, 'Nidhi', 78);")
    cur.execute("INSERT INTO STUDENT VALUES (4, 'Nikhil', 55);")
    cur.execute("INSERT INTO STUDENT VALUES (5, 'Deepti', 95);")
    print('Data Inserted Successfully!!')

    conn.commit()
    
    # Retrieving data from table
    print('Output of Select Queries')
    print('Retrieving roll numbers, names, and percentages of students')
    cur.execute('SELECT RollNum, Name, Percentage FROM\
    STUDENT;')
    print(cur.fetchall())
          
    print('Retrieving all attribute values of students')
    cur.execute('SELECT * FROM STUDENT;')
    print(cur.fetchall())
          
    print('Retrieving roll numbers and names of students')
    cur.execute('SELECT RollNum, Name FROM STUDENT;')
    print(cur.fetchall())
          
    print('Retrieving all attribute values of students with\
    percentage greater than 80')
    cur.execute('SELECT * FROM STUDENT WHERE Percentage > 80;')
    print(cur.fetchall())

    # Close the connection
    conn.close()
    

if __name__ == '__main__':
  main()
