from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://treehouse-projects.github.io/horse-land/index.html')

time.sleep(5) # to give js time to run

page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html.parser')

print(soup.prettify())

driver.close()