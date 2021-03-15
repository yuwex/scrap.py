from model import Model
from controller import Controller
from action import Action
from part import Part
import os

class View:

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        
        self.game_loop()

    

    def wait_for_start(self):
        os.system('clear')
        print('Scrapyard-MVC, CLI, No Abilities')
        input('[Press Enter to Begin]\n>')

    def create_players(self):
        while True:
            os.system('clear')
            maxplayers = input('how many players do you want? (2 - 8)\n>')
            if maxplayers.isdigit():
                maxplayers = int(maxplayers)
                if maxplayers > 2 and maxplayers < 8:
                    break
            
            else:
                print('You entered something wrong.')
        
        names = []
        for i in range(1, maxplayers + 1):
            os.system('clear')
            name = input(f'Enter player {i}\'s name\n>')
            while True:
                if name in names:
                    print('Someone else already has that name.')
                elif input(f'Are you okay with the name {name}? (y/n)\n>').upper() == 'Y':
                    break
                name = input(f'Enter player {i}\'s name\n>')
            names.append(name)
        
        self.controller.create_players(names)

    def turn_options(self):
        turn = self.controller.get_current_turn()
        
        while True:
            print(f'\nIt\'s {self.controller.get_players()[turn]}\'s turn.')
            ans = self.choose_from(['View player', 'View scrapyard', 'Take turn'])
            if ans == 'View player':
                self.view_player()
            if ans == 'View scrapyard':
                self.view_scrap()
            if ans == 'Take turn':
                self.take_turn(turn)


        # self.controller.take_turn(self.model.players[turn], parts_rm_flaw, Action.TakePart, )


    def view_player(self):
        ans = self.choose_from(self.controller.get_players(), return_type=int)
        player = self.controller.get_player(ans)
        print(f'Stats for player: {player.name}\nGold: {player.gold}')
        print('Robot')
        for part_type, part_list in player.robot.get_robot().items():
            print(f'Part Type: {part_type}')
            if part_list:
                for part in part_list:
                    print(f' - {part}')
            else:
                print(' - Empty')
        self.wait_input()

    def view_scrap(self):
        print('Scrapyard:')
        for part in self.controller.get_scrapyard().get_parts():
            print(f' - {part.__dict__}')
        self.wait_input()


    def take_turn(self, turn):
        
        # ask for 2 parts rm flaw
        flaw_parts = self.controller.get_player_flaw(turn)
        parts_remove_flaw = []


        if len(flaw_parts) == 0:
            print('There were no flaws to remove.')
        else:
            ans = self.controller.choose_from(flaw_parts + ['Skip'], 'Choose a part to remove 1 flaw from or skip [1/2]')
            if not ans is 'Skip':
                parts_remove_flaw.append(ans)
                ans = self.controller.choose_from(flaw_parts + ['Skip'], 'Choose a part to remove 1 flaw from or skip [2/2]')
                if not ans is 'Skip':
                    parts_remove_flaw.append(ans)


        
        # choose action

        # rm 1 flaw

        # gain 2 gold

        # obtain card

        action = self.controller.choose_from(['Remove 1 repair counter', 'Gain 2 gold', 'Obtain a card'])
        if(action == 'Remove 1 repair counter'):
            self.robot.remove_flaws(1)
        elif(action == 'Gain 2 gold'):
            self.gold += 2
            print('Gained 2 gold.\nYou now have ' + str(self.gold) + ' gold.') 
        elif(action == 'Obtain a card'):
            card_chosen = self.controller.choose_from(scrapyard.cards)
            ans = self.controller.choose_from(['Yes', 'Go Back'], text='Are you sure you want to get ' + card_chosen.get_name() + '?\nGold cost: ' + str(card_chosen.get_gold()) + '\nFlaws: ' + str(card_chosen.get_flaw()))
            if(ans == 'Yes'):
                scrapyard.take_part(self, card_chosen)

        # player: Player, parts_rm_flaw: list, action: Action, action_part: Part=None, part_location: str=None, part_use_gold: bool=None

        self.controller.take_turn()

    def wait_input(self, text='[Enter]'):
        input(text)

    def choose_from(self, item_list, text='Which item do you choose?', end='\n> ', return_type = str):
            
        text = '\n' + text + '\n'
        i = 1
        
        for item in item_list:
            if(type(item) == Part):
                text += (str(i) + ': ' + item.display() + '\n')
            else:
                text += (str(i) + ': ' + str(item) + '\n')
            i += 1


        while(True):
            ans = False
            try:
                ans = int(input(text + end))
                if(ans > 0):
                    if return_type is str:
                        ans = item_list[ans-1]
                else:
                    ans = False
            except:
                print('Bad Input')
                ans = False

            if(ans):
                if return_type is int:
                    ans = ans - 1
                break
        
        return ans

    def get_confirm_input(self, text, confirm_text='Is this answer ok? (y / n)'):
        confirm = ''
        while not confirm.lower() == 'y':
            ans = input(text)
            confirm = input(confirm_text)
        return ans
        


    def game_loop(self):
        self.wait_for_start()
        # self.create_players()
        self.turn_options()
        # self.view_player()

