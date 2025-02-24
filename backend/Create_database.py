import sqlite3
import os

# Define the database file name
db_file = 'student.sqlite3'

# Check if the database file already exists, and remove it if it does
if os.path.exists(db_file):
    os.remove(db_file)

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the 'groups' table
cursor.execute('''
CREATE TABLE "groups" (
    "GroupID" INTEGER PRIMARY KEY,
    "GroupName" TEXT NOT NULL,
    "MajorID" INTEGER NOT NULL
)
''')

# Create the 'majors' table
cursor.execute('''
CREATE TABLE "majors" (
    "MajorID" INTEGER PRIMARY KEY,
    "MajorName" TEXT NOT NULL
)
''')

# Create the 'payments' table
cursor.execute('''
CREATE TABLE "payments" (
    "payment_id" INTEGER PRIMARY KEY,
    "student_index" INTEGER NOT NULL,
    "Amount" REAL NOT NULL,
    "PaymentDate" TEXT NOT NULL
)
''')

# Create the 'students' table
cursor.execute('''
CREATE TABLE "students" (
    "student_index" INTEGER PRIMARY KEY,
    "FirstName" TEXT NOT NULL,
    "LastName" TEXT NOT NULL,
    "MajorID" INTEGER NOT NULL,
    "GroupID" INTEGER NOT NULL,
    FOREIGN KEY ("MajorID") REFERENCES "majors" ("MajorID"),
    FOREIGN KEY ("GroupID") REFERENCES "groups" ("GroupID")
)
''')

# Create the 'totals' table
cursor.execute('''
CREATE TABLE "totals" (
    "student_index" INTEGER PRIMARY KEY,
    "amount_due" REAL NOT NULL,
    FOREIGN KEY ("student_index") REFERENCES "students" ("student_index")
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database '{db_file}' created successfully with the required tables.")