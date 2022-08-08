# The below code is creating a table called Cars and inserting the values from the csv file into the
# table.
import mysql.connector
import csv

# Connecting to the database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", # Your db password
    database="CarRentalDatabase"
)

# Creating a cursor object.
mycursor = mydb.cursor()

# Creating a table called Cars and inserting the values from the csv file into the table.
try:
    mycursor.execute("CREATE TABLE Cars (CarID VARCHAR(255), \
    CarBrand VARCHAR(255),\
    Available VARCHAR(255))")

except:
    pass

# This is reading the csv file and inserting the values into the table.
with open("cars.csv", "r")as csvfile:
    csvdata = csv.reader(csvfile, delimiter=",")
    for row in csvdata:
        sql = "INSERT INTO Cars VALUES (%s, %s ,%s)"
        val = (row[0], row[1], row[2])
        mycursor.execute(sql, val)
        mydb.commit()

# This is printing the values from the table.
mycursor.execute("select * from Cars")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)