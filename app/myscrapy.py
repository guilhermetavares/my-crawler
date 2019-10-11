
from app.tasks import tasks_process_url
from app.soup import Crawler

url_ = 'https://www.epocacosmeticos.com.br/'
tasks_process_url.delay(url_)
