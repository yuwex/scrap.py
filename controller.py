from part import Part
from player import Player
from model import Model
from action import Action
import os
import random

from model import Model

class Controller:

    def __init__(self, model: Model):
        self.model = model

    # cannot have 2 of same name, cannot have more than 8 names, cannot have less than 2 names
    def create_players(self, name_list):
        
        player_golds = []
        for i in range(2, len(name_list) + 2): # pylint: disable=unused-variable
            player_golds.append(i)
        
        self.model.create_players(name_list, player_golds)

    # check if player is right player
    def take_turn(self, player: Player, parts_rm_flaw: list, action: Action, part: Part = None, tp_location: str = None, tp_use_gold: bool = None):



        if parts_rm_flaw:
            if not len(parts_rm_flaw) == 0:
                #parts rm flaw is: (part obj)
                #check not more 2
                for part in parts_rm_flaw:
                    part.remove_flaw(1)
            

        if action is Action.RemoveFlaw:
            # action controls = part to remove from
            # check if part can remove flaw, if part belongs to said player
            part.remove_flaw(1)

        if action == Action.GainGold:
            # action = None
            player.change_gold()
            

        if action == Action.TakePart:
            
            # action controls = {'part': Part, 'location': 'loc', 'use_gold':True}
            # check if part can be bought, location correct, part correct

            location = tp_location
            use_gold = tp_use_gold

            if part in self.model.scrapyard.get_parts():
                if use_gold:
                    player.change_gold(-part.get_gold())
                    part.remove_flaw(part.get_flaw())
                self.model.scrapyard.remove_part(part)
                player.robot.add_part(part, location)



p1 = Player('test', 2)
mod = Model()
con = Controller(mod)
con.take_turn(p1, [], Action.TakePart)

# TODO: Action controls



        # if action is remove 1 repair...
        # if action is gain 2 gold...
        # if action is obtain a card...


# c = Controller()
# c.create_players([])

    # def choose_from(self, item_list, text='Which item do you choose?', end='\n> '):
        
    #     text = '\n' + text + '\n'
    #     i = 1
        
    #     for item in item_list:
    #         if(type(item) == Part):
    #             text += (str(i) + ': ' + item.display() + '\n')
    #         else:
    #             text += (str(i) + ': ' + str(item) + '\n')
    #         i += 1


    #     while(True):
    #         ans = False
    #         try:
    #             ans = int(input(text + end))
    #             if(ans > 0):
    #                 ans = item_list[ans-1]
    #             else:
    #                 ans = False
    #         except:
    #             print('Bad Input')
    #             ans = False

    #         if(ans):
    #             break
        
    #     return ans

    # def wait_input(self, text='[ENTER]'):
    #     input(text)
    
    # def get_confirm_input(self, text, confirm_text='Is this answer ok? (y / n)'):
    #     confirm = ''
    #     while not confirm.lower() == 'y':
    #         ans = input(text)
    #         confirm = input(confirm_text)
    #     return ans