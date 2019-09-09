import re
from urllib.parse import urljoin

import feedparser
from bs4 import BeautifulSoup
import requests
from dateutil.parser import parse


from exchange.models import CurrencyRate


class ECBScraper:
    """
    European Central Bank page rrs scrapper.
    Reading Euro exchange rates compared to other currencies
    """
    def __init__(self):
        self.base_url = 'https://www.ecb.europa.eu/'

    def find_rss_currency_pages(self):
        response = requests.get(urljoin(self.base_url, 'home/html/rss.en.html'))
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('a', attrs={'href': re.compile("^/rss/fxref")})

    def scrap_page(self, link):
        feed = feedparser.parse(urljoin(self.base_url, link))
        for post in feed.entries:
            date = parse(post['updated'])
            exchange_rate = post['cb_exchangerate'].split('\n')[0]
            currency = post['cb_targetcurrency']
            CurrencyRate.objects.get_or_create(
                date=date,
                currency=currency,
                defaults=(
                    dict(exchange_rate=exchange_rate)
                )
            )

    def scrap(self):
        for page in self.find_rss_currency_pages():
            self.scrap_page(page['href'])
