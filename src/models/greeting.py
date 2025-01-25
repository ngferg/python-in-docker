import json
from src.dao.counter import Counter

class Greeting(object):
    def __init__(self, name: str):
        self.message = f'Hello, {name}!'
        counter = Counter()
        self.count = counter.get(name=name)
        counter.set(name=name, val=self.count + 1)


    def json(self) -> str:
        return json.dumps(self.__dict__)
