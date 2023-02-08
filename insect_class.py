import random


class insect:
    def __init__(self):
        self.leg = 4
        self.wing = 2
        self.mile = 0

    def fly(self):
        self.mile = random.randint(1, 10)

    def get_fly(self):
        return self.mile
