import random


class insect:


    def __init__(self,n,w,l):
        self.name = n
        self.wing = w
        self.leg = 1
        self.mile = 0

    def fly(self):
        self.mile = random.randint(1, 10)

    def get_fly(self):
        return self.mile

    def get_name(self):
        return self.name 
