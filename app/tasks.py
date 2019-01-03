from __future__ import absolute_import

import os
import time, requests

from slugify import slugify

from app.celery import app
from app.soup import Crawler
from app.cache_walrus import set_item_data, get_visited_links, \
    append_visited_links, pop_processing


crawler = Crawler()

@app.task
def tasks_process_url(url):
    print('&' * 100)
    print('url')
    print('tasks_process_url', slugify(url))

    if url in get_visited_links():
        return

    links = crawler.get_links(url)

    append_visited_links(url)

    if links:
        for link in links:
            tasks_process_url.delay(link)
        process_detail_url.delay()


@app.task
def process_detail_url():
    link = pop_processing()

    if link:
        data = crawler.get_data(link)
        set_item_data(data)
        process_detail_url.delay()
    else:
        # process
        pass
