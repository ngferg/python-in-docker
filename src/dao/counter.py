from src.config.redis import Redis

class Counter(object):
    def __init__(self):
        self.connection = Redis().get_connection()

    def set(self, name: str, val: int):
        self.connection.set(name, val)

    def get(self, name: str) -> int:
        counter = self.connection.get(name)
        return int(counter) if counter else 0
