import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Crawler(object):

    def get_soup(self, url):
        contents = requests.get(url).content
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

    def get_links(self, url):
        soup = self.get_soup(url)
        links = [link.get('href') for link in soup.findAll('a', attrs={'href': re.compile("/")})]
        return links

    def get_data(self, url):

        soup = self.get_soup(url)

        mydivs = soup.find("div", {"class": "productName"})
        name = mydivs.text

        mydivs = soup.find("strong", {"class": "skuBestPrice"})
        price = mydivs.text

        mydivs = soup.find("meta", {"name": "Abstract"})
        title = mydivs.get('content')

        return {
            'name': name,
            'price': price,
            'title': title,
            'url': url,
        }
