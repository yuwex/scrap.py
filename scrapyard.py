from part import Part
from player import Player
from deck import Deck

class Scrapyard:
    def __init__(self, card_list=[]):
        self.cards = card_list
    
    def __str__(self):
        val = 'Scrapyard: \n'
        for card in self.cards:
            if(card == self.cards[-1]):
                val += card.display(True)
            else:
                val += card.display(True) + '\n'
        
        return val
    
    def take_part(self, player, part, allowed=['b', 's']):
        
        
        ans = ''
        while(not (ans == 'b' or ans == 's')):
            if(player.gold >= part.gold):
                ans = input('Would you like to buy (b) or salvage (s) this part? (b, s): ')

            if ans not in allowed:
                ans = ''
                print('You are not allowed to obtain this part in that way.')

            elif(player.gold < part.gold):
                input('You do not have enough gold to buy this part, so you will salvage it [ENTER]')
                ans = 's'
                break
        
            if(ans == 'b'):
                print(str(part.gold) + 'G has been reducted from your account.')
                player.gold -= part.gold
                part.flaw = 0
                break



        player.robot.add_part(part)

        if part in self.cards:
            self.cards.remove(part)



    def add_parts(self, parts):
        if(type(parts) == list):
            for part in parts:
                self.cards.append(part)
        elif(type(parts) == Part):
            self.cards.append(part)
        else:
            print('Error: Not a list or Part')
            print(type(parts))
    
    def add_deck(self, deck, num=1):
        cards = deck.take_card(num)
        self.add_parts(cards)

# print(scrap)

