import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=San-Francisco'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="SearchResults")
# print(results.prettify())
job_elems = results.find_all(
    'section', class_='card-content')  # returns an iterable

for job in job_elems:  # each job is a new BeautifulSoup object
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text, end='\n'*2)

python_jobs = results.find_all(
    'h2', string=lambda text: 'python' in text.lower())

print(len(python_jobs))

for p_job in python_jobs:
	link = p_job.find('a')['href']
	print(p_job.text.strip())
	print(f"Apply here: {link}\n")