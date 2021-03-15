from robot import Robot
from part import Part

class Player:
    def __init__(self, name='empty', gold=0, identity=0):
        self.name = name
        self.gold = gold
        self.robot = Robot()
        self.identity = identity

    def __str__(self):
        return self.name

    def change_gold(self, gold=2):
        self.gold += gold
