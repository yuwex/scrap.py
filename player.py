from robot import Robot
from part import Part

class Player:
    def __init__(self, name='empty', gold=0):
        self.name = name
        self.gold = gold
        self.robot = Robot()

    def change_gold(self, gold=2):
        self.gold += gold
