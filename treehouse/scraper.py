from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')
# beautiful soup doesn't wait for JS to run before scraping the page

divs = soup.find_all('div', {'class': 'featured'})
# for div in divs:
	# print(div.text)

featured_header = soup.find('div', {'class': 'featured'}).h2
# print(featured_header.get_text())

# find & find_all take the following parameters:
# name - looks for tags with certain names such as div or a
# attrs - css classes
# recursive - default 'true' looks at all siblings, 'false' looks at children only
# string - search for strings instead of tags
# **kwargs - search for other items such as search id
# limit - find is find_all with limit set to 1

# for button in soup.find(attrs={'class': 'button--primary'}): same as
# for button in soup.find(class_='button--primary'): 
# 	print(button)

# for link in soup.find_all('a'):
# 	print(link.get('href'))

# ------------------------------ Crawling pages ------------------------------ #

