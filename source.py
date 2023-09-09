import json
import requests 

url_data = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json"
url_replace = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json"

response = requests.get(url_data)
data = response.json()

response = requests.get(url_replace)
replaceItems = response.json()

result = []

for str in data:
    result.append(str)
    replace = str
    for it in replaceItems:
        if (result[len(result) - 1] == it["replacement"]):
            replace = it["source"]
    if (replace == None):
        result.pop()
    else:
        result[len(result) - 1] = replace

with open ("result.json", "w") as write:
    json.dump(result, write, indent=1)