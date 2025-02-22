import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import time
import random



import sqlite3

import sqlite3




def check_adjacent_id_and_dept(db_path, target_string):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all (id, dept) pairs from the class table
    words = target_string.split()
    print(words)
    for word in range(len(words)):
        print(word)
        if(word < len(words)-1):
            cursor.execute("SELECT * FROM class WHERE dept = '" + words[word] + "' AND id = " + words[word+1])
    
            class_data = cursor.fetchall()  # List of tuples (id, dept)
            print(class_data)
            return True, words[word], words[word+1]




def insert_class(id, name, dept):
    # Connect to the SQLite database
    conn = sqlite3.connect("./CCSC_Hackathon_Miz/college.db")
    cursor = conn.cursor()

    # SQL query to insert a new class
    cursor.execute('''
        INSERT OR IGNORE INTO class (id, name, dept)
        VALUES (?, ?, ?)
    ''', (id, name, dept))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Class {name} added successfully!")

def insert_prereq(id, prereq):
    # Connect to the SQLite database
    conn = sqlite3.connect("./CCSC_Hackathon_Miz/college.db")
    cursor = conn.cursor()

    # SQL query to insert a new class
    cursor.execute('''
        INSERT OR IGNORE INTO prereqs (class_id, prereq_id)
        VALUES (?, ?)
    ''', (id, prereq))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Prereq {prereq} added successfully!")



all_depts = []
url = "https://catalog.missouri.edu/courseofferings/"  # Replace with your target URL
headers = {"User-Agent": "Mozilla/5.0"}  # Helps avoid getting blocked
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")


soup = BeautifulSoup(response.text, "html.parser")

# Find the div with id "codepartments"
dept_div = soup.find("div", id="co_departments")

if dept_div:
    # Find all <a> tags within the div
    links = dept_div.find_all("a")
    
    # Extract text from each <a> tag
    for link in links:
        text = link.text.strip()

        
        all_depts.append(text.split()[-1].split("(")[1].split(")")[0])


else:
    print("Div with id 'codepartments' not found")




    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS prereqs (
    #         class_id TEXT NOT NULL,
    #         prereq_id TEXT NOT NULL,
    #         PRIMARY KEY (class_id, prereq_id),
    #         FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
    #         FOREIGN KEY (prereq_id) REFERENCES class(id) ON DELETE CASCADE
    #     )
    # ''')
missed = []
all_depts = ["cmp_sc"]
for dept in all_depts:


    url = "https://catalog.missouri.edu/courseofferings/" + dept.lower()  # Replace with your target URL
    headers = {"User-Agent": "Safari/537.36"}  # Helps avoid getting blocked
    try:
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            print("Page fetched successfully!")
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")


        soup = BeautifulSoup(response.text, "html.parser")

        classes = soup.find_all(class_ = "courseblock")
        
        for c in classes:
            
            coursetitle = c.select_one(".courseblocktitle")  # Get the first matching element

            coursetitle = coursetitle.text.strip() # Print the text content

            stringify = c.select_one(".courseblockdesc").get_text(strip=True)


            # credit_hours = re.split("Credit Hours: |Credit Hour:", stringify)[1][0]
            prereq = 0
            prereqs = []
            try:
                prereq = stringify.split("Prerequisites:")[1].split("Recommen")[0]
            except: 
                try:
                    prereq = stringify.split("Prerequisites:")[1]
                except:
                    pass
            
            print(coursetitle + " " + prereq)
                        # Example usage:

            found, found_id, found_dept = check_adjacent_id_and_dept("./CCSC_Hackathon_Miz/college.db", prereq)
            print(prereq)
            if found:
                print(f"Found adjacent class ID and department: {found_id} ({found_dept})")
                insert_prereq(coursetitle.split(": ")[0].split()[0] + coursetitle.split(": ")[0].split()[1], found_dept + found_id)
           
            else:
                print("No matching adjacent class ID and department found in string.")
                print(prereq)

            
    except:
        missed.append(dept)
print(missed)
# for link in links:



#     url = "https://catalog.missouri.edu" + link["href"]

#     response = requests.get(url, headers=headers)

#     classinfo = BeautifulSoup(response.text, "html.parser")

#     credit_hours_match = re.search(r"Credit Hour[s]*:\s*(\d+)", soup.text)

#     prereq_match = re.search(r"Prerequisites:\s*([^<]+)", soup.text)

#     class_title = classinfo.select_one(".search-courseresult h3").get_text(strip=True)

#     stringify = classinfo.select_one(".courseblockdesc").get_text(strip=True)


#     credit_hours = re.split("Credit Hours: |Credit Hour:", stringify)[1][0]
#     prereq = 0
#     prereqs = []
#     try:
#         prereq = stringify.split("Prerequisites:")[1].split("Recommen")[0]
#     except: 
#         try:
#             prereq = stringify.split("Prerequisites:")[1]
#         except:
#             pass
    


#     class_desc = stringify.split("Credit Hour")[0]
#     print("Credit Hours: ", credit_hours)
#     print("prereq: ", prereq)
#     print("title: ", class_title)
#     print("Description: ", class_desc)


#     insert_class(class_title.split(": ")[0].split()[1], class_title.split(": ")[1], class_title.split(": ")[0].split()[0])


# Example of adding a new class


    #Credit Hour</strong><strong>s</strong>:


