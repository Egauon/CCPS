import requests
from bs4 import BeautifulSoup
import re




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
links=["A"]
for link in links:


    url = "https://catalog.missouri.edu" + "/search/?P=BIO_SC%203650"

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
        prereq = stringify.split("Prerequisites:")[1].split(" in ")
        prereq.pop(0)
        for pre in prereq:
            prereqs.append(pre.split(" ")[0] + " " + pre.split(" ")[1][0:4])
    except:
        try:
            prereqs.append(stringify.split("Prerequisites:")[1].split(" standing ")[0])
        except:
            prereqs = []


    class_desc = stringify.split("Credit Hour")[0]
    print("Credit Hours: ", credit_hours)
    print("prereq: ", prereqs)
    print("title: ", class_title)
    print("Description: ", class_desc)

    #Credit Hour</strong><strong>s</strong>:

