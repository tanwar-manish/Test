import requests
import json

url = "https://reqres.in/api/users?page="
payload = {}
headers = {}

totalUsers = 0
finished = False
page = 1
while not finished:
    response = requests.request("GET", url + str(page), headers=headers, data=payload)
    users = json.loads(response.text)
    totalUsers += len(users.get("data"))
    if len(users.get("data")) == 0:
        finished = True
    else:
        page += 1
print(totalUsers)
