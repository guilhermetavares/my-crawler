from __future__ import absolute_import
from app.celery import app
import time, requests
from pymongo import MongoClient


client = MongoClient('mongo', 27018)

print('*' * 100)

@app.task
def longtime_add(self, i):
    print('long time task begins', i)
