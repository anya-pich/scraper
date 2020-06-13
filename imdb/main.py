import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:

    # Name
    name = container.h3.a.text
    titles.append(name)

    # year
    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)

    # time
    runtime = container.p.find('span', class_='runtime').text if container.p.find(
        'span', class_='runtime').text else '-'
    time.append(runtime)

    # IMDb rating
    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    # metascore
    m_score = container.find('span', class_='metascore').text if container.find(
        'span', class_='metascore') else '-'
    metascores.append(m_score)

    # here are two NV containers, grab both of them as they hold both the votes and the grosses
    nv = container.find_all('span', attrs={'name': 'nv'})

    # filter nv for votes
    vote = nv[0].text
    votes.append(vote)

    # filter nv for gross
    grosses = nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)

print(titles)
print(years)
print(time)
print(imdb_ratings)
print(metascores)
print(votes)
print(us_gross)

movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
})

print(movies)

# clean the data!
print(movies.dtypes)  # check data types
# go into movies dataframe year column, extract digits and cast as integer
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].astype(int)
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['us_grossMillions'] = movies['us_grossMillions'].map(
    lambda x: x.lstrip('$').rstrip('M')) # anonymous function
movies['us_grossMillions'] = pd.to_numeric(
    movies['us_grossMillions'], errors='coerce') # coerces non-numbers to NaNs

print(movies)
print(movies.dtypes)

movies.to_csv('movies.csv')
