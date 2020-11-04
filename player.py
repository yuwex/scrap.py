from robot import Robot
from part import Part

class Player:
    def __init__(self, name='empty', gold=0):
        self.name = name
        self.gold = gold
        self.robot = Robot()

    
    def __str__(self):
        return self.name + ', ' + str(self.gold) + ', ' + self.robot.__str__()
    
    def take_turn(self, scrapyard, deck):
        self.robot.remove_flaws(2, True, True)

        action = self.robot.choose_from(['Remove 1 repair counter', 'Gain 2 gold', 'Obtain a card'])
        if(action == 'Remove 1 repair counter'):
            self.robot.remove_flaws(1)
        elif(action == 'Gain 2 gold'):
            self.gold += 2
            print('Gained 2 gold.\nYou now have ' + str(self.gold) + ' gold.') 
        elif(action == 'Obtain a card'):
            card_chosen = self.robot.choose_from(scrapyard.cards)
            ans = self.robot.choose_from(['Yes', 'Go Back'], text='Are you sure you want to get ' + card_chosen.get_name() + '?\nGold cost: ' + str(card_chosen.get_gold()) + '\nFlaws: ' + str(card_chosen.get_flaw()))
            if(ans == 'Yes'):
                scrapyard.take_part(self, card_chosen)
        
        scrapyard.add_parts(deck.take_card())

#if no cards missing in scrapyard 