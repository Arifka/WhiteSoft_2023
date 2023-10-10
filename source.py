import json
import requests 
import output

url_data = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json"
url_replace = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json"

response = requests.get(url_data)
data = response.json()

response = requests.get(url_replace)
replaceItems = response.json()

result = []
sizeRepItems = len(replaceItems)

for str in data:
    for indPair in range(sizeRepItems):
        repEl = replaceItems[sizeRepItems - 1 - indPair]["replacement"]
        sourceEl = replaceItems[sizeRepItems - 1 - indPair]["source"]
        if (repEl in str):
            if (sourceEl is None):
                str = str.replace(repEl, "")
            else:
                str = str.replace(repEl, sourceEl)
    result.append(str)

output.write_data2json(result)