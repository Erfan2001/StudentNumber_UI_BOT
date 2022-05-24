import requests
from bs4 import BeautifulSoup, Tag
import json
baseURL = "http://lms.ui.ac.ir/profile/"
# incoming_years = ["97", "98", "99", "400"]
incoming_years = ["97"]
field_code = '36'
# incoming_type = ['13', '23', '63']
incoming_type = ['13']
headers = {"Cookie": """PHPSESSID=fpun2q59b8ifslu08fkcjb59n3; cc_loggedin=1"""}
users = []
def calculate():
    for i in incoming_years:
        for j in incoming_type:
            for k in range(1, 3):
                studentNumber = """%s%s%s%s""" % (
                    i, field_code, j, (3-len(str(k)))*'0'+str(k))
                print(studentNumber)
                response = requests.get("""%s%s""" % (
                    baseURL, studentNumber), headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "lxml")
                    data_name = soup.find_all("h2")
                    name = data_name[0].string.strip()
                    data = soup.find_all("img", {"class": "thumb_profile"})
                    image = "http://lms.ui.ac.ir"+data[0].get("src")
                    users.append({"studentNumber": studentNumber,
                                 "name": name, "image": image})
                else:
                    print("Error")
    res = {"result": users}
    with open('users.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=4))
