import json
import requests 
import output
import solver

url_data = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json"
url_replace = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json"

response = requests.get(url_data)
data = response.json()

response = requests.get(url_replace)
replaceItems = response.json()

result = solver(replaceItems, data)
output.write_data2json(result)