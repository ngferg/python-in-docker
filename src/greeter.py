from src.models.greeting import Greeting

class Greeter(object):
    def hello_world(self) -> str:
        return self.greet('World')

    def greet(self, name: str) -> str:
        greeting = Greeting(name)
        return greeting.json()

    def reset(self, name: str) -> str:
        greeting = Greeting(name)
        greeting.reset()
        return greeting.json()
