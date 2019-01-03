from walrus import Database
REDIS_URL = 'redis://redis:6379'
db = Database.from_url(REDIS_URL)
cache = db.cache()


def get_visited_links():
    return cache.get('visited', None) or []


def append_visited_links(link):
    visited = cache.get('visited', None) or []
    cache.set('visited', visited + [link])

    processing = cache.get('processing', None) or []
    cache.set('processing', processing + [link])


def set_item_data(data):
    if data:
        data = cache.get('data', None) or []
        cache.set('data', data + [data])


def pop_processing():
    pop_link = None
    processing = cache.get('processing', None) or []

    if processing:
        pop_link = processing.pop()
        cache.set('processing', processing)

    return pop_link
