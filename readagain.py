import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('college_minor.db')
cursor = conn.cursor()

# Fetch and print data from MINOR table
cursor.execute('SELECT * FROM MINOR')
minors = cursor.fetchall()
print("Minors:")
for minor in minors:
    print(minor)

# Fetch and print data from minor_courses table
cursor.execute('SELECT * FROM minor_courses')
courses = cursor.fetchall()
print("\nCourses:")
for course in courses:
    print(course)

# Fetch and print data from minor_categories table
cursor.execute('SELECT * FROM minor_categories')
categories = cursor.fetchall()
print("\nCategories:")
for category in categories:
    print(category)

# Close the connection
conn.close()
