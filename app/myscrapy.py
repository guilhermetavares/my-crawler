print('*' * 20)
import asyncio

from soup import Crawler

url_ = 'https://www.epocacosmeticos.com.br/'

crawler = Crawler()
links = crawler.get_links(url_)

for l in links:
    print(l)

url_ = 'https://www.epocacosmeticos.com.br/212-nyc-men-vintage-body-spray-carolina-herrera-perfume-masculino-para-o-corpo/p'
crawler = Crawler()
data_ = crawler.get_data(url_)


print('*' * 20)
