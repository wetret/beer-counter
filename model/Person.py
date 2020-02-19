class Person:
    name = ''
    count = 0

    def __init__(self, name):
        self.name = name

    def increase(self):
        self.count = self.count + 1

    def decrease(self):
        if self.count > 0:
            self.count = self.count - 1