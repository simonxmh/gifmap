import http.client
import json

conn = http.client.HTTPConnection("content.guardianapis.com")


headers = {
    'cache-control': "no-cache",
    'postman-token': "4c7a9cf4-6dbc-445f-f2b3-892f00da7ced"
    }

conn.request("GET", "/search?q="+"china"+"&api-key=ac013d68-5be5-4324-b54f-989a650a4d31&format=json&show-elements=image&pageSize=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

with open('data.txt','w') as outfile:
	json.dump(data.decode("utf-8"),outfile)

