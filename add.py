import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('college_minor.db')
cursor = conn.cursor()

# Insert data for "Minor in Accountancy"
minor_name = "Minor in Accountancy"
total_hours = 15  # Total required credit hours for the minor

# Insert minor into the MINOR table
cursor.execute('''
INSERT INTO MINOR (name, total_hours) 
VALUES (?, ?)
''', (minor_name, total_hours))

# Get the minor_id of the newly inserted minor
minor_id = cursor.lastrowid

# Insert required courses for the minor into the minor_courses table
required_courses = [
    ('ACCTCY 2036', 'Accounting I', 3, 1),  # Required course
    ('ACCTCY 2037', 'Accounting II', 3, 1),  # Required course
    ('ACCTCY 2258', 'Computer-Based Data Systems', 3, 1),  # Required course
    ('ACCTCY 4356', 'Financial Accounting Concepts', 3, 1),  # Required course
    ('ACCTCY 3326', 'Financial Accounting Theory and Practice I', 3, 0),  # Optional course (part of the OR set)
    ('ACCTCY 3346', 'Financial Accounting Theory and Practice II', 3, 0),  # Optional course (part of the OR set)
]

# Insert elective courses (optional courses)
elective_courses = [
    ('ACCTCY 3328', 'Accounting Information Systems', 3, 0),  # Optional elective
    ('ACCTCY 3347', 'Cost and Managerial Accounting', 3, 0),  # Optional elective
    ('ACCTCY 4353', 'Introduction to Taxation', 3, 0),  # Optional elective
]

# Combine required and elective courses
all_courses = required_courses + elective_courses

# Insert courses into the minor_courses table
for course in all_courses:
    cursor.execute('''
    INSERT INTO minor_courses (minor_id, course_id, course_name, credits, required) 
    VALUES (?, ?, ?, ?, ?)
    ''', (minor_id, course[0], course[1], course[2], course[3]))

# Insert minor categories (for required and elective courses)
category_name = "Required Courses"
required_hours = 12  # Required hours for the core courses
category_dept = "School of Accountancy"

cursor.execute('''
INSERT INTO minor_categories (minor_id, category_name, required_hours, dept) 
VALUES (?, ?, ?, ?)
''', (minor_id, category_name, required_hours, category_dept))

category_name = "Elective Courses"
required_hours = 3  # Required hours for electives

cursor.execute('''
INSERT INTO minor_categories (minor_id, category_name, required_hours, dept) 
VALUES (?, ?, ?, ?)
''', (minor_id, category_name, required_hours, category_dept))

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()

print("Data has been successfully added to the database.")
