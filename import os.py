import os

FILE_NAME = "hotel_bookings.txt"

# -----------------------------
# Function to Add Booking
# -----------------------------
def add_booking():
    print("\n----- New Booking -----")

    name = input("Enter Customer Name: ")
    phone = input("Enter Mobile Number: ")
    room = input("Enter Room Number: ")

    print("\nRoom Types")
    print("1. Standard - ₹1000/day")
    print("2. Deluxe - ₹2000/day")
    print("3. AC Deluxe - ₹3000/day")

    choice = input("Select Room Type (1-3): ")

    if choice == "1":
        room_type = "Standard"
        price = 1000
    elif choice == "2":
        room_type = "Deluxe"
        price = 2000
    elif choice == "3":
        room_type = "AC Deluxe"
        price = 3000
    else:
        print("Invalid Room Type!")
        return

    days = int(input("Enter Number of Days: "))

    total = price * days
    gst = total * 0.18
    final_bill = total + gst

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{room},{room_type},{days},{final_bill}\n")

    print("\nBooking Successful")
    print("----------------------")
    print("Customer :", name)
    print("Room :", room)
    print("Room Type :", room_type)
    print("Days :", days)
    print("Total Bill : ₹", round(final_bill, 2))


# -----------------------------
# View Bookings
# -----------------------------
def view_bookings():

    if not os.path.exists(FILE_NAME):
        print("\nNo Booking Found.")
        return

    print("\n----------- BOOKINGS -----------")

    with open(FILE_NAME, "r") as file:

        data = file.readlines()

        if len(data) == 0:
            print("No Booking Available")
            return

        for record in data:
            name, phone, room, roomtype, days, bill = record.strip().split(",")

            print("--------------------------------")
            print("Name :", name)
            print("Phone :", phone)
            print("Room :", room)
            print("Room Type :", roomtype)
            print("Days :", days)
            print("Bill : ₹", bill)


# -----------------------------
# Search Customer
# -----------------------------
def search_customer():

    if not os.path.exists(FILE_NAME):
        print("No Records Found.")
        return

    search = input("Enter Customer Name: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:

        for record in file:

            name, phone, room, roomtype, days, bill = record.strip().split(",")

            if name.lower() == search:
                print("\nCustomer Found")
                print("-------------------")
                print("Name :", name)
                print("Phone :", phone)
                print("Room :", room)
                print("Room Type :", roomtype)
                print("Days :", days)
                print("Bill : ₹", bill)

                found = True

    if not found:
        print("Customer Not Found.")


# -----------------------------
# Delete Booking
# -----------------------------
def delete_booking():

    if not os.path.exists(FILE_NAME):
        print("No Booking Found.")
        return

    name = input("Enter Customer Name to Delete: ").lower()

    records = []
    found = False

    with open(FILE_NAME, "r") as file:

        for record in file:

            data = record.strip().split(",")

            if data[0].lower() != name:
                records.append(record)
            else:
                found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if found:
        print("Booking Deleted Successfully.")
    else:
        print("Customer Not Found.")


# -----------------------------
# Main Program
# -----------------------------
while True:

    print("\n====================================")
    print("      HOTEL MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Add Booking")
    print("2. View Bookings")
    print("3. Search Customer")
    print("4. Delete Booking")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_booking()

    elif choice == "2":
        view_bookings()

    elif choice == "3":
        search_customer()

    elif choice == "4":
        delete_booking()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice!")