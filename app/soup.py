import requests
import re

from walrus import Database
from bs4 import BeautifulSoup
from urllib.parse import urlparse

REDIS_URL = 'redis://redis:6379'
db = Database.from_url(REDIS_URL)
cache = db.cache()


class Crawler(object):
    REGEX_URL = re.compile(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$')

    def _get_cache_data(self, key):
        return cache.get(key, None) or []

    def _set_visited_links(self, link):
        visited = self._get_cache_data('visited')
        cache.set('visited', visited + [link])

        processing = self._get_cache_data('processing')
        cache.set('processing', processing + [link])

    def save(self, item):
        if item:
            data = self._get_cache_data('data')
            cache.set('data', data + [item])

    def pop(self):

        pop_link = None
        processing = self._get_cache_data('processing')

        if processing:
            pop_link = processing.pop()
            cache.set('processing', processing)

        return pop_link

    def get_soup(self, link):
        contents = requests.get(link).content
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

    def assert_product_link(self, link, regex='.*?/p$'):
        return len(re.compile(regex).findall(link)) > 0

    def format_link(self, link, parse_url):
        href = link.get('href')

        if self.REGEX_URL.match(href):
            if re.search(parse_url.netloc, href):
                return href
            return None
        # abs
        return parse_url.scheme + '://' + parse_url.netloc + href

    def get_links(self, link):

        if link in self._get_cache_data('visited'):
            return []

        self._set_visited_links(link)

        soup = self.get_soup(link)
        if soup is None:
            return []

        parse_url = urlparse(link)

        links = list()
        for link in soup.findAll('a', attrs={'href': re.compile("/")}):
            _formated_link = self.format_link(link, parse_url)

            if _formated_link:
                links.append(_formated_link)

        return set(links)


    def get_data(self, link):

        if not self.assert_product_link(link):
            return {}

        soup = self.get_soup(link)

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
            'url': link,
        }
