from os import getenv
from cachelib.redis import RedisCache

class Cache:

    def __init__(self):
        host = getenv("REDIS_HOST")
        port = getenv("REDIS_PORT")
        self.redis = RedisCache(host=host, port=port)
        
    def get(self, key: str):
        return self.redis.get(key)

    def put(self, key: str, value, time: str) -> bool:
        self.redis.add(key, value, time) 
        return True

    def forget(self, key: str) -> bool:
        return self.redis.delete(key)

