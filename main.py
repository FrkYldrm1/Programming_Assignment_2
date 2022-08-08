# The code below is the main application
import mysql.connector as mysql

# Connecting to the database.
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="CarRentalDatabase"
)

# Creating a cursor object.
mycursor = mydb.cursor()
mycursor = mydb.cursor(buffered=True)

while True:
    # Main menu
    print("----------------------------------------------------------------")
    print("Main Menu")
    print("Select one of the Options : ")
    print("----------------------------------------------------------------")
    print(" press 1 : if you are an employee")
    print(" press 2 : if you are a new customer")
    print(" press 3 : if you are a want more informatioon about our services")
    print(" press 4 : if you want to stop the application4")


    # Taking the input from the user and converting it to an integer.
    value = int(input("Enter: "))
    print("----------------------------------------------------------------")

    # Case 1
    if value == 1:
        print("Please enter you name: ")
        name = str(input("Enter: "))

        # We get the date of the needed employee
        mycursor.execute(f"select * from Employees where Name ='{name}'")
        myresult = mycursor.fetchall()

        # This is a loop that goes through the results of the query and gets the data from the table.
        employeeID = 0
        employeeName = ""
        employeeEmail = ""
        for x in myresult:
            # Getting the data from the table.
            employeeID = x[0]
            employeeName = x[1]
            employeeEmail = x[2]

        print("What would you like to do?")
        print("----------------------------------------------------------------")
        print("press 1: to view your information")
        print("press 2: to see the taken cars + their customers")
        print("press 3: to create a view of the available cars")

        # Taking the input from the user and converting it to an integer.
        newIn = int(input("Enter: "))
        print("----------------------------------------------------------------")
        if newIn == 1:

            # Printing the data from the table.
            print(f"EmployeeID: {employeeID}")
            print(f"Name: {employeeName}")
            print(f"Email: {employeeEmail}")
            print("----------------------------------------------------------------")

        elif newIn == 2:
            # This query gets the car and joins it with their customer's data
            mycursor.execute(f"SELECT Cars.CarBrand, Customers.Name, Customers.Email FROM Cars INNER JOIN Customers ON Customers.CarWanted = Cars.CarBrand;")
            myresult = mycursor.fetchall()
            for x in myresult:
                    # Display the date
                    print(f"CarBrand: {x[0]}", "|", f"Name: {x[1]}", "|", f"Email: {x[2]}")
                    print("--------------------------------------------------------")

        elif newIn == 3:
            # This query creates a view of the available cars
            mycursor.execute(f"CREATE OR REPLACE VIEW Available AS SELECT Cars.CarID, Cars.CarBrand, Cars.Available from Cars where available = 'TRUE';")
            mycursor.execute(f"select * from Available;")
            myresult = mycursor.fetchall()
            print(myresult)
            print("----------------------------------------------------------------")

        # A simple error message that is displayed when the user enters an invalid input.
        else:
            print("Invalid input")

    # Case 2
    elif value == 2:
        #We get the customer name and email address
        name = input("Enter name: ")
        email = input("Enter email: ")

        # We check what cars are available
        mycursor.execute(f"select * from Cars where Available ='TRUE'")
        myresult = mycursor.fetchall()

        # Printing the available cars.
        for x in myresult:
            print("Available Car: ",x[1])

        print("----------------------------------------------------------------")

        #The user inputs the wanted car
        car = input("Enter car: ")

        # This is a query that inserts the values to the table.
        sql = "INSERT INTO Customers VALUES (%s, %s ,%s)"
        val = (name, email, car)
        mycursor.execute(sql, val)

        #We change the car's availability status to false
        sql = f"UPDATE Cars SET Available = 'FALSE' WHERE CarBrand = '{car}';"
        mycursor.execute(sql)

        print("Operation was successful, you will be contacted by an employee soon")
        print("----------------------------------------------------------------")

    # Case 3
    elif value== 3:
        #We display the employees that are currently working
        print("Contact:")
        mycursor.execute(f"select * from Employees where Working ='YES'")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(f"Name: {x[1]}", "|", f"Email: {x[2]}")
            print("--------------------------------------------------------")
    elif value == 4:
        break

    # Waiting for the user to press any key to go to the main menu.
    wait = input("press any key to go to main menu: ")


