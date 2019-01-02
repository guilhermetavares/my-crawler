from walrus import Database

REDIS_URL = 'redis://redis:6379'
db = Database.from_url(REDIS_URL)
cache = db.cache()


def get_visited_links():
    return cache.get('visited', None) or []


def append_visited_links(link):
    visited = cache.get('visited', None) or []
    cache.set('visited', visited + [link])
