import random

class DiceObject:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        result = random.randint(1,self.sides)
        return result
