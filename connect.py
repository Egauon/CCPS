import sqlite3

def connect_to_db():
    # Connect to the SQLite database
    conn = sqlite3.connect("./CCSC_Hackathon_Miz/college.db")
    cursor = conn.cursor()
    
    # Example query to retrieve all classes
    # cursor.execute('''SELECT * FROM id''')
    
    # # Fetch all results
    # rows = cursor.fetchall()
    
    # # Print the results
    # for row in rows:
    #     print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    connect_to_db()



