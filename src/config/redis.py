import redis
import os

class Config(object):
    def __init__(self):
        self.redis_host = os.getenv('redis_host')
        self.redis_port = os.getenv('redis_port')

class Redis(object):
    def get_connection(self):
        config = Config()
        return redis.Redis(host=config.redis_host, port=config.redis_port, decode_responses=True)

