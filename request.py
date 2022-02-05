
import requests
import json

url = 'http://127.0.0.1:5000/results'

data = [[ 308.7, 7767, 56]]
j_data = json.dumps(data)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
response = requests.post(url, data=j_data, headers=headers)
print(response,response.text)
