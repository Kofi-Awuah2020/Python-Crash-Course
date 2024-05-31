"""Modelling a Die"""
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides), end="\t")


first_die = Die()
second_die = Die(10)
for roll in range(10):
    first_die.roll_die()
    second_die.roll_die()
    print()