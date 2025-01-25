from src.models.greeting import Greeting

class Greeter(object):
    def hello_world(self) -> str:
        return self.greet('World')

    def greet(self, name: str) -> str:
        greeting = Greeting(f'Hello, {name}!')
        return greeting.json()

