'''5. Provide a program to create tables (Employee, Department,
Project) in database Sqlite and insert the data.
• Make sure to add basic field, with employee to department and project relation.
• Make sure maintain M2M relation between employee and project'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Department(did INT PRIMARY KEY, departmentname VARCHAR(20);")
mycursor.execute("CREATE TABLE Project(pid INT PRIMARY KEY, department VARCHAR(10),FOREIGN KEY (department) REFERENCES Department (did);")
mycursor.execute("CREATE TABLE Employee(eid INT PRIMARY KEY, employeename VARCHAR(20), department VARCHAR(10), project VARCHAR(10),FOREIGN KEY (department) REFERENCES Department (did),FOREIGN KEY (project) REFERENCES Project (pid);")

