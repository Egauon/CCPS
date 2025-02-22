import sqlite3

def read_classes():
    # Connect to the SQLite database
    conn = sqlite3.connect("./CCSC_Hackathon_Miz/college.db")
    cursor = conn.cursor()

    # SQL query to select all rows from the class table
    cursor.execute('''SELECT * FROM class WHERE dept = 'ABM' AND id = 2223''')


    # Fetch all results
    rows = cursor.fetchall()

    # Print each row (class)
    for row in rows:
        print(f"Class ID: {row[0]}, Name: {row[1]}, Department: {row[2]}")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    read_classes()
