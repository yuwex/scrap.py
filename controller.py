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
    def create_players(self, name_list: list):
        
        if name_list > 8 or name_list < 2:
            raise Exception('name_list must be between 8 and 2 (inclusive)')

        player_golds = []
        for i in range(2, len(name_list) + 2): # pylint: disable=unused-variable
            player_golds.append(i)

        self.model.create_players(name_list, player_golds)

    # check if player is right player
    def take_turn(self, player: Player, parts_rm_flaw: list, action: Action, action_part: Part = None, part_location: str = None, part_use_gold: bool = None):

        if parts_rm_flaw:
            
            for part in parts_rm_flaw:
                
                if len(parts_rm_flaw) > 2:
                    raise Exception('parts_rm_flaw is too long')

                if not isinstance(part, Part):
                    raise Exception('parts_rm_flaw has non-part object')

                if not player.robot.find_part(part):
                    raise Exception('parts_rm_flaw part does not belong to player')

        if action == Action.RemoveFlaw:
            
            if action_part.get_flaw() < 1:
                raise Exception('You cannot remove flaws from parts without flaws')
                    
            if not player.robot.find_part(action_part):
                raise Exception('action_part not owned by player')

        if action == Action.TakePart:
            
            # check if part can be bought, location correct, part correct
            if not action_part.is_buyable:
                raise Exception('The specified part cannot be bought')

            if player.robot.check_location(part_location) is False:
                raise Exception('The specified location was either not found or full')

            if not action_part in self.model.scrapyard.get_parts():
                raise Exception('The specified part is not in the scrapyard')

            if part_use_gold and action_part.get_gold() > player.gold:
                raise Exception('The player does not have enough gold to purchace this part')
 
        if action == Action.RemoveFlaw:
            action_part.remove_flaw(1)

        if action == Action.GainGold:
            player.change_gold()

        if action == Action.TakePart:

            location = part_location
            use_gold = part_use_gold

            if action_part in self.model.scrapyard.get_parts():
                if part_use_gold:
                    player.change_gold(-action_part.get_gold())
                    action_part.remove_flaw(action_part.get_flaw())
                self.model.scrapyard.remove_part(action_part)
                player.robot.add_part(action_part, part_location)

        for part in parts_rm_flaw:
            part.remove_flaw(1)


p1 = Player('test', 2)
mod = Model()
con = Controller(mod)
mod.scrapyard.parts[0] = Part('joe', 5, 5, 'cell')
print(Part('joe', 5, 5, 'cell').get_gold())

con.take_turn(p1, [], Action.TakePart, action_part=mod.scrapyard.parts[0], part_location='leg', part_use_gold=True)

print(p1.__dict__)

for p in p1.robot.get_all_parts():
    print(p.__dict__)

# TODO: Action controls
