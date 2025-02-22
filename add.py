import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('college_minor.db')
cursor = conn.cursor()

# Insert data for MINOR table
cursor.execute('''
INSERT INTO MINOR (name, total_hours) 
VALUES (?, ?)
''', ('Minor in Mathematics', 15))

# Commit the insertion for MINOR table
conn.commit()

# Fetch the minor_id for use in other tables
cursor.execute('''
SELECT id FROM MINOR WHERE name = ?
''', ('Minor in Mathematics',))
minor_id = cursor.fetchone()[0]

# Insert data for minor_courses table (required core courses and optional courses)
courses = [
    ('MATH 1500', 'Introductory Calculus I', 3, 1),
    ('MATH 1700', 'Introductory Calculus II', 3, 1),
    ('MATH 2300', 'Introduction to Linear Algebra', 3, 1),
    ('MATH 2320', 'Calculus for Engineers', 3, 0),
    ('MATH 3000', 'Advanced Calculus', 3, 0),
    ('MATH 4000', 'Abstract Algebra', 3, 0)
]

for course in courses:
    cursor.execute('''
    INSERT INTO minor_courses (minor_id, course_id, course_name, credits, required)
    VALUES (?, ?, ?, ?, ?)
    ''', (minor_id, course[0], course[1], course[2], course[3]))

# Commit the insertion for minor_courses table
conn.commit()

# Insert data for minor_categories table
categories = [
    ('Core Courses', 9, 'Mathematics', None),  # Core courses category, 9 credit hours, Mathematics dept
    ('Advanced Courses', 6, None, 4000)  # Advanced courses category, 6 required credit hours, 4000-level
]

for category in categories:
    cursor.execute('''
    INSERT INTO minor_categories (minor_id, category_name, required_hours, dept, min_number)
    VALUES (?, ?, ?, ?, ?)
    ''', (minor_id, category[0], category[1], category[2], category[3]))

# Commit the insertion for minor_categories table
conn.commit()

# Close the connection
conn.close()
