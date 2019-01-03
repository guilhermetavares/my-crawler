print('*' * 20)

from app.tasks import longtime_add, tasks_process_url
from app.soup import Crawler

url_ = 'https://www.epocacosmeticos.com.br/'

tasks_process_url.delay(url_)

# crawler = Crawler()
# links = crawler.get_links(url_)
# ALREADY_URL = [
#     url_,
# ]
#
# for l in links:
#     print(l)

# for href in links:
#
#     if href in ALREADY_URL:
#         continue
#
#     ALREADY_URL.append(href)
#
#     for i in crawler.get_links(href):
#         print(i)
#
#
#
# for l in links:
#     print(l)
#
# url_ = 'https://www.epocacosmeticos.com.br/212-nyc-men-vintage-body-spray-carolina-herrera-perfume-masculino-para-o-corpo/p'
# crawler = Crawler()
# data_ = crawler.get_data(url_)
#

print('*' * 20)
