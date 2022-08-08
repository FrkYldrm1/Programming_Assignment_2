# The above code is creating a table called Employees and then inserting the data from the csv file
# into the table.
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", #Your db password
    database="CarRentalDatabase"
)

# Creating a cursor object that is used to traverse the records from the result set.
mycursor = mydb.cursor()

# Creating a table called Employees and then inserting the data from the csv file
# into the table.
try:
    mycursor.execute("CREATE TABLE Employees (EmployeeID VARCHAR(255), \
    Name VARCHAR(255),\
    Email VARCHAR(255),\
    Working VARCHAR(255))")

except:
    pass

with open("employees.csv", "r")as csvfile:
    csvdata = csv.reader(csvfile, delimiter=",")

    for row in csvdata:
        sql = "INSERT INTO Employees VALUES (%s, %s ,%s, %s)"
        val = (row[0], row[1], row[2], row[3])
        mycursor.execute(sql, val)
        mydb.commit()

# Printing the data from the table.
mycursor.execute("select * from Employees")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)