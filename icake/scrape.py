import requests
from bs4 import BeautifulSoup

s = requests.Session()
results = requests.get("https://www.interviewcake.com/table-of-contents")
soup = BeautifulSoup(results.text, "html.parser")
main = soup.find('div', class_='toc')

print(main.get_text())