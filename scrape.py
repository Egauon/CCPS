import requests
from bs4 import BeautifulSoup
import re
import sqlite3

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



url = "https://catalog.missouri.edu/collegeofengineering/computerscience/bs-computer-science/#mpr"  # Replace with your target URL
headers = {"User-Agent": "Mozilla/5.0"}  # Helps avoid getting blocked
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")


soup = BeautifulSoup(response.text, "html.parser")


links = soup.find_all("a", href=lambda x: x and "/search/?" in x)

for link in links:


    url = "https://catalog.missouri.edu" + link["href"]

    response = requests.get(url, headers=headers)

    classinfo = BeautifulSoup(response.text, "html.parser")

    credit_hours_match = re.search(r"Credit Hour[s]*:\s*(\d+)", soup.text)

    prereq_match = re.search(r"Prerequisites:\s*([^<]+)", soup.text)

    class_title = classinfo.select_one(".search-courseresult h3").get_text(strip=True)

    stringify = classinfo.select_one(".courseblockdesc").get_text(strip=True)


    credit_hours = re.split("Credit Hours: |Credit Hour:", stringify)[1][0]
    prereq = 0
    prereqs = []
    try:
        prereq = stringify.split("Prerequisites:")[1].split("Recommen")[0]
    except: 
        try:
            prereq = stringify.split("Prerequisites:")[1]
        except:
            pass
    


    class_desc = stringify.split("Credit Hour")[0]
    print("Credit Hours: ", credit_hours)
    print("prereq: ", prereq)
    print("title: ", class_title)
    print("Description: ", class_desc)


    insert_class(class_title.split(": ")[0].split()[1], class_title.split(": ")[1], class_title.split(": ")[0].split()[0])


# Example of adding a new class


    #Credit Hour</strong><strong>s</strong>:


