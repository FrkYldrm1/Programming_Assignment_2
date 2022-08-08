# The below code is creating a table called Customers and inserting the values from the csv file into
# the table.
import mysql.connector
import csv

# Connecting to the database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", #Your db password
    database="CarRentalDatabase"
)

# Creating a cursor object.
mycursor = mydb.cursor()

# Creating a table called Customers and inserting the values from the csv file into the table.
try:
    mycursor.execute("CREATE TABLE Customers (Name Varchar(255),\
    Email VARCHAR(255), \
    CarWanted VARCHAR(255),\
    PRIMARY KEY (Name))")

except:
    pass

# This is reading the csv file and inserting the values into the table.
with open("customers.csv", "r")as csvfile:
    csvdata = csv.reader(csvfile, delimiter=",")
    for row in csvdata:
        sql = "INSERT INTO Customers VALUES (%s, %s, %s)" # we insert the values to the table.
        val = (row[0], row[1], row[2])
        mycursor.execute(sql, val)
        mydb.commit()

# Printing the values from the table.
mycursor.execute("select * from Customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)