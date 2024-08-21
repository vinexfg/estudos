import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3001/estudos_pv/#footer'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parsed')


top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
print(top_jobs_heading)