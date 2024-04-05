# fareRates of cities
import os

adminName = "admin"
adminPassword = "admin"
bookings = {}

# names of cities
cityNames = ["Ahmedabad", "Delhi", "Mumbai", "Hyderabad", "Chennai", "Bengaluru"]


fareRates = [[0, 8000, 19000, 4560, 3000, 1950],  # Ahmedabad
             [8000, 0, 10500, 6500, 2000, 1000],  # Delhi
             [19000, 10500, 0, 25500, 30000, 5500],  # Mumbai
             [4560, 6500, 25500, 0, 4000, 7000],  # Hyderabad
             [3000, 2000, 30000, 4000, 0, 1500],  # Chennai
             [1950, 1000, 5500, 7000, 1500, 0],]  # Bengaluru

# seats of cities avilable
seatsAvailable = [[0, 50, 50, 50, 50, 50],  
                  [50, 0, 50, 50, 50, 50], 
                  [50, 50, 0, 50, 50, 50],  
                  [50, 50, 50, 0, 50, 50],  
                  [50, 50, 50, 50, 0, 50],  
                  [50, 50, 50, 50, 50, 0],]


# heading() shows the title bar

def heading(title):
    print('\033c')
    line = "----------------------------------------------------------------"
    print(line)
    print(title.center(len(line)))
    print(line, "\n")


def options():
    line = "-----------------"
    print(line)
    print("Press the key to")
    print(line)

    print("1- To know travel details ")
    print("2- To book your seat")
    print("3- To print your ticket")
    print("4- To cancel the booking ")
    print("5- Admin")
    print("0- to exit")
    print(line)
# main_functions(int) check out the selected function
# and call the respective function
    option = int(input())
    main_functions(option)


# travelDetails() shows the travel details of names of cites their fares and seats available
def travelDetails():
    heading("Travel Details")
    print("Fare of cities are: \n")

    # Print column headers
    """ print("{:<10}".format(""), end="") """
    for city in cityNames:
        print(city)
        """ print("{:<10}".format(city), end="") """
    print()

    # Print rows with city names and fares
    for i, city in enumerate(cityNames):
        print(city)
        """ print("{:<10}".format(city), end="") """
        print("|", end='')

        for j in range(6):
            print(fareRates[i][j])
            """ print("{:<10}".format(fareRates[i][j]), end="") """
        print()

    print("\n\nAvailable no of seats are : \n")
    
    # Print column headers
    """ print("{:<10}".format(""), end="") """
    for city in cityNames:
        print(city)
        """ print("{:<10}".format(city), end="") """
    print()

    # Print rows with city names and no of seats
    for i, city in enumerate(cityNames):
        print(city)
        """ print("{:<10}".format(city), end="") """
        print("|", end='')

        for j in range(6):
            print(seatsAvailable[i][j])
            """ print("{:<10}".format(seatsAvailable[i][j]), end="") """
        print()

    print("\n\n")
    options()

# createRecipt() creates recipt of the booking

def createRecipt(name, email, phoneNumber, travelingCity, destination, noOfSeats):
    fare = fareRates[travelingCity][destination]*noOfSeats

    # Create the receipt file
    filename = f"receipt_{name}.txt"
    if os.path.exists(filename):
        print("Ticket already exists with this name.")
        ch=input("Enter 1 to redirect to Home page:")
        if ch=='1':
            first_page()
        else:
            return
    else:
        heading("Recipt")
        line="________________________________"
        with open(filename, "w") as f:
            f.write(line)
            f.write("\n")
            f.write(line)
            f.write(f"\nName : {name}\n")
            f.write(f"Email : {email}\n")
            f.write(f"Phone Number : {phoneNumber}\n")
            f.write(f"Traveling From : {cityNames[travelingCity]}\n")
            f.write(f"Destination : {cityNames[destination]}\n")
            f.write(f"Number of tickets : {noOfSeats}\n")
            f.write(f"Fare per seat is : {fareRates[travelingCity][destination]}\n")
            f.write(f"Total fare : {fare}\n")
            f.write(line)
            f.write("\n")

        print(f"Receipt saved as {filename}")
        input("\nTo go back press 1 :")

def ticketprint(name):
    filename = f"receipt_{name}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    print(line.strip())
                print()
        options()
    else:
        print("No ticket found for this name.")
        print("Directing to Home page.")
        first_page()

# functon seatBooking() to book seats for travel


def seatBooking():
    heading("Seat Booking")

    # code to take booking details
    name = input("Full Name : ")
    email = input("Email : ")
    while True:
        try:
            phoneNumber = int(input("Phone Number : "))
            break
        except ValueError:
            print("Invalid phone number. Please enter a valid number.")

    # take detail of traveling city
    while(True):
        print("\nYou want to travel from : ")
        for i in range(0, 6):
            print(i+1, "-", cityNames[i])
        travelingCity = int(input("\n")) - 1

        # take detail of destination city
        print("\n\nYour destination is : ")
        for i in range(0, 6):
            print(i+1, "-", cityNames[i])
        destination = int(input("\n")) - 1

        if travelingCity==destination:
            print("Cannot travel to same city.")
            ch=input(print("To try again enter 1:"))
            if ch=="1":
                continue
            else:
                print("Redirecting you to home page...")
                first_page()
                
        else:
            noOfSeats = int(input("\nNo of seats you want to book : "))
            confirmation = int(input("To confirm your booking press 1 else 0 : "))

            # checks confirmation if true then calls createRecipt function
            # else call to the home page
            if confirmation == 0:
                first_page()
            else:
                # update no of availability of seats
                seatsAvailable[travelingCity][destination] = seatsAvailable[travelingCity][destination]-noOfSeats

                if name in bookings:
                    print("ticket already booked")
                else:
                    bookings[name]=noOfSeats

                    # create recipt
                createRecipt(name, email, phoneNumber,travelingCity, destination, noOfSeats)
                options()

# function to cancelbooking to cancel ticket booking


def cancelBooking():
    heading("Cancel Booking")

    # take detail of traveling city
    print("\nYou were traveling from : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    # take detail of destination city
    print("\n\nYour destination was : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    name = input("Enter Name from your Ticket : ")
    noOfSeats = int(input("\nNo of seats you want to cancel : "))
    confirmation = int(input("To cancel your booking press 1 else 0 : "))
    filename = f"receipt_{name}.txt"

    # checks confirmation if true then updates the number of available seats
    # else call to the home page
    flag=True
    if confirmation == 0:
        first_page()
    else:
        while(flag):
            if name in bookings:
                if noOfSeats==bookings[name]:
                    del bookings[name]
                    if os.path.exists(filename):
                        os.remove(filename)
                        print("\nYour booking has been cancelled")
                    else:
                        print("ticket not found. Redirecting to Home page....")
                        first_page()
                    # update no of availability of seats
                    seatsAvailable[travelingCity][destination] = seatsAvailable[travelingCity][destination]+noOfSeats
                    options()
                else:
                    print("Entered number of seats didn't match with your booking.")
                    ch=int(input(print("To try again enter 1:")))
                    if  ch==1:
                        cancelBooking()
                    else:
                        flag=False
            else:
                print("Entered name didn't have any bookings")
                while(True):
                    ch=int(input(print("Do You Want To Go Back? Enter 1: ")))
                    if ch==1:
                        first_page()
                    else:
                        print("invalid input")
                        continue



# fuction for admin accessibility and admin options


def admin():
    heading("Admin")

    # code for admin functionality
    userName = input("User Name : ")
    password = input("Enter password :")

    if (userName == adminName and password == adminPassword):
        adminOptions()
    else:
        print("Wrong credentials ")
        next = int(
            input("To enter again press 1 or return to home page press 0 : "))
        if next == 1:
            admin()
        else:
            first_page()


def adminOptions():
    heading("admin")
    print("Press key to :")
    print("1- Update No of seats")
    print("2- Update fare rates")
    print("3- Update admin details")
    print("4- Return to Home page")
    print("0- To exit")

    user_input = int(input("\n"))
    if user_input == 0:
        exit()
    elif user_input == 1:
        updateSeats()
        adminOptions()
    elif user_input == 2:
        updateRates()
        adminOptions()

    elif user_input == 3:
        updateAdminDetails()
        adminOptions()

    elif user_input == 4:
        first_page()
    else:
        first_page()


def updateSeats():
    print("Update availble seat deatails of : ")
    print("\n City : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    print("\nTo city : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    newSeats = int(input("Enter new number of avaialable seats are :"))
    seatsAvailable[travelingCity][destination] = newSeats
    print("Seats have been updated")
    input("\Go back press 1")


def updateRates():
    print("Update fare deatails of : ")
    print("\n City : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    print("\nTo city : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    newFareRates = int(input("Enter new fare rates are :"))
    fareRates[travelingCity][destination] = newFareRates
    print("Fare rates have been updated")
    input("\Go back press 1")


def updateAdminDetails():
    print("Update Admin deatails :")

    updatedAdminName = input("Enter new username :")
    updatedAdminPassword = input("Enter new password :")

    global adminName
    global adminPassword

    adminName = updatedAdminName
    adminPassword = updatedAdminPassword
    print("\nAdmin username and password have been updated")
    input("\nGo back press 1 :")


# main_function checkout the options and calls the repective function


def main_functions(user_input):
    if user_input == 0:
        exit()
    elif user_input == 1:
        travelDetails()
    elif user_input == 2:
        seatBooking()
    elif user_input == 3:
        name=input("Enter your Name : ")
        ticketprint(name)
    elif user_input == 4:
        cancelBooking()
    elif user_input == 5:
        admin()
    else:
        print("Invalid Option")
        first_page()

def first_page():
    heading("Welcome to Indian Express")
    options()

# main function
# while to keep it until it is exited


def main():
    while True:
        first_page()


main()
