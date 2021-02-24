from part import Part
from robot import Robot
from player import Player
from deck import Deck
from scrapyard import Scrapyard


class Model:

    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.scrapyard = Scrapyard(self.deck.take_card(4))

    def create_players(self, player_names, player_golds):
        if len(player_names) == len(player_golds):
            for i in range(len(player_names)):
                self.players.append(Player(name = player_names[i], gold = player_golds[i]))
        else:
            print('error')
    
