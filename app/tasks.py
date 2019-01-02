from __future__ import absolute_import

import os
import time, requests

from app.celery import app
from app.soup import Crawler
from app.cache_walrus import get_visited_links


@app.task
def tasks_process_url(url):

    if url in get_visited_links():
        return

    crawler = Crawler()
    links = crawler.get_links(url)

@app.task
def process_detail_url(url):
    visited_links = cache.get('')
