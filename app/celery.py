from __future__ import absolute_import
from celery import Celery

app = Celery(
    'app',
    broker='amqp://admin:password@rabbit:5672',
    backend='rpc://',
    include=['app.tasks'])
