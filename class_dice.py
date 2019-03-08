import random
class dice:
    def __init__(self, sides):
        self.sides = int(sides)
    def roll(self):
        result = random.randint(1,self.sides)
        return result