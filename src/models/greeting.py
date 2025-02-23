import json
from src.dao.counter import Counter
from flask import jsonify

class Greeting(object):
    def __init__(self, name: str):
        self.message = f'Hello, {name}!'
        self.counter = Counter()
        self.count = self.counter.get(name=name)
        self.counter.set(name=name, val=incer(self.count))
        self.name = name

    def reset(self):
        self.count = 0
        self.counter.set(self.name, 0)


    def json(self) -> str:
        return jsonify({
            'message': self.message,
            'count': self.count,
        })

incer = lambda x: x + 1