from __future__ import absolute_import

import os
import time, requests

from slugify import slugify

from app.celery import app
from app.soup import Crawler


crawler = Crawler()

@app.task
def tasks_process_url(url):
    print('&' * 100)
    print('url')
    print('tasks_process_url', slugify(url))

    links = crawler.get_links(url)

    if links:
        for link in set(links):
            tasks_process_url.delay(link)
        process_detail_url.delay()


@app.task
def process_detail_url():
    link = crawler.pop()

    if link:
        data = crawler.get_data(link)
        crawler.save(data)
        process_detail_url.delay()
    else:
        # process
        pass
