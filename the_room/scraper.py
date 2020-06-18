import requests
from bs4 import BeautifulSoup

url = "https://medium.com/@DavidKlion/full-transcript-of-the-room-341e4286db8e"
results = requests.get(url)
soup = BeautifulSoup(results.text, "html.parser")

# text in em tags
ems = []
# dialog text that begins with name colon
dialog = []

paragraphs = soup.find_all('p')

for each in paragraphs:
	if each.find('em'):
		ems.append(each.find('em').text)
	else:
		dialog.append(each.text)

print(ems[:10])
print(len(ems))
print(dialog[:10])
print(len(dialog))
