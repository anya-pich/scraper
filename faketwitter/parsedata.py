import json

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
#     print (i['date'])
	if "obama" in i['tweet'].lower():
		print(i)