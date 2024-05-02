import csv
import psycopg2 as pgsql


connection = pgsql.connect(host="localhost", dbname="phone", user="postgres",
                           password="08082006", port=5432)
cur = connection.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number INT
);
""")


def search_records(pattern):
    cur.execute("""
        SELECT surname, name, number
        FROM PhoneBook
        WHERE surname ILIKE %s OR name ILIKE %s OR CAST(number AS TEXT) LIKE %s
    """, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    return cur.fetchall()


def insert_or_update_user(surname, name, phone):
   
    cur.execute("""
        SELECT * FROM PhoneBook WHERE surname = %s AND name = %s
    """, (surname, name))
    if cur.fetchone():
     
        cur.execute("""
            UPDATE PhoneBook SET number = %s WHERE surname = %s AND name = %s
        """, (phone, surname, name))
    else:
       
        cur.execute("""
            INSERT INTO PhoneBook (surname, name, number) VALUES (%s, %s, %s)
        """, (surname, name, phone))

def delete_by_surname_or_phone(identifier):
    cur.execute("""
        DELETE FROM PhoneBook
        WHERE surname = %s OR CAST(number AS TEXT) = %s
    """, (identifier, identifier))

# INSERTING DATA--------------------------

mode = "enter"
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    print("enter surname:")
    surname = input()
    print("enter name:")
    name = input()
    print("enter number:")
    phone = input()
    insert_or_update_user(surname, name, phone)

# INSERT CSV-----------------
while True:
    print("Want to insert data from csv file? yes/no:")
    mode=input()
    if mode=="no":
        break
    print("enter the name of the file")
    mode=input()
    with open("C:/Users/Nurai/PP2/LAB11/data.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)",row)




# SEARCHING DATA--------------

while True:
    print("Type 'search' to search for records or 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    print("Enter search pattern:")
    pattern = input()
    results = search_records(pattern)
    for row in results:
        print(row)

# DELETING DATA-----------
while True:
    print("want to delete some data? yes/no")
    mode = input()
    if mode == "no":
        break
    print("Enter surname or phone number to delete:")
    identifier = input()
    delete_by_surname_or_phone(identifier)


connection.commit()
cur.close()
connection.close()