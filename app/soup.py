import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Crawler(object):
    REGEX_URL = re.compile(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$')

    def get_soup(self, url):
        contents = requests.get(url).content
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

    def format_link(self, link, parse_url):
        href = link.get('href')

        if self.REGEX_URL.match(href):
            if re.search(parse_url.netloc, href):
                return href

        # abs
        return parse_url.scheme + '://' + parse_url.netloc + href

    def get_links(self, url):
        soup = self.get_soup(url)
        parse_url = urlparse(url)

        links = list()

        for link in soup.findAll('a', attrs={'href': re.compile("/")}):
            _formated_link = self.format_link(link, parse_url)
            if _formated_link:
                links.append(_formated_link)

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
