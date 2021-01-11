from robot import Robot
from part import Part
from controller import Controller

class Player:
    def __init__(self, name='empty', gold=0):
        self.name = name
        self.gold = gold
        self.robot = Robot()
        self.controller = Controller()


