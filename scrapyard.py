from part import Part
from player import Player
from deck import Deck

class Scrapyard:
    def __init__(self, card_list=[]):
        self.parts = card_list

    def get_parts(self):
        return self.parts

    def add_parts(self, parts):
        if(type(parts) == list):
            for part in parts:
                self.parts.append(part)
        elif(type(parts) == Part):
            self.parts.append(part)
    
    def remove_part(self, part):
        if part in self.parts:
            self.parts.remove(part)

    
    def add_deck(self, deck, num=1):
        cards = deck.take_card(num)
        self.add_parts(cards)
    


# print(scrap)

