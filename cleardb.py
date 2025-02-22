import sqlite3

def clear_table():
    # Connect to the SQLite database
    conn = sqlite3.connect("./CCSC_Hackathon_Miz/college.db")
    cursor = conn.cursor()

    # SQL query to delete all rows from the 'class' table
    cursor.execute('''DELETE FROM class''')
    
    # Commit the changes
    conn.commit()

    # Optionally, print confirmation
    print("All records in the 'class' table have been deleted.")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    clear_table()
