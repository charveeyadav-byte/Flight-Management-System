import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="your_password",
database="flightdb"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flights(
flight_no VARCHAR(10) PRIMARY KEY,
source VARCHAR(50),
destination VARCHAR(50),
seats INT
)
""")

while True:
  print("\n===== FLIGHT MANAGEMENT SYSTEM =====")
  print("1. Add Flight")
  print("2. View Flights")
  print("3. Search Flight")
  print("4. Delete Flight")
  print("5. Exit")

```
choice = input("Enter Choice: ")

if choice == "1":
    flight_no = input("Flight Number: ")
    source = input("Source: ")
    destination = input("Destination: ")
    seats = int(input("Seats Available: "))

    sql = "INSERT INTO flights VALUES(%s,%s,%s,%s)"
    values = (flight_no, source, destination, seats)

    cursor.execute(sql, values)
    conn.commit()

    print("Flight Added Successfully")

elif choice == "2":
    cursor.execute("SELECT * FROM flights")

    records = cursor.fetchall()

    for row in records:
        print(row)

elif choice == "3":
    flight_no = input("Enter Flight Number: ")

    cursor.execute(
        "SELECT * FROM flights WHERE flight_no=%s",
        (flight_no,)
    )

    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Flight Not Found")

elif choice == "4":
    flight_no = input("Enter Flight Number: ")

    cursor.execute(
        "DELETE FROM flights WHERE flight_no=%s",
        (flight_no,)
    )

    conn.commit()

    print("Flight Deleted Successfully")

elif choice == "5":
    break

else:
    print("Invalid Choice")
```

conn.close() 


CREATE DATABASE flightdb;

USE flightdb;

