import json

class Greeting(object):
    def __init__(self, message: str):
        self.message = message

    def json(self) -> str:
        return json.dumps(self.__dict__)
