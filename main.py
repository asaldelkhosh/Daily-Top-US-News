from bs4 import BeautifulSoup
import requests
from kafka import KafkaProducer
import datetime


URL = "https://www.nbcnews.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

spans = soup.find_all('span', {'class': 'tease-card__headline'})

producer = KafkaProducer(bootstrap_servers='')
date = str(datetime.datetime.now().date())

for span in spans:
    print(span.get_text())
    producer.send(date, span.get_text())
