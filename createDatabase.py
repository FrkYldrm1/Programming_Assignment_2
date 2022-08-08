# Creating a database called CarRentalDatabase.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", #Your db password

)

mycursor = mydb.cursor()
mycursor.execute("create database CarRentalDatabase")

