from part import Part
from player import Player
from robot import Robot
from deck import Deck
from scrapyard import Scrapyard
from abilities import AbilityManager
from controller import Controller

import random
import os

class GameManager:

    def __init__(self):
        os.system('clear')

        self.controller = Controller()
        self.players = self.create_players()
        self.deck = Deck()
        self.deck.shuffle()


        #part = Part('rich mint-condition cat head', 0, 100, 'head', 'mew mew may the gods bless you')
        #deck.replace_top(part)
        self.scrapyard = Scrapyard()
        self.scrapyard.add_deck(self.deck, 4)
        
    def get_players(self, min_players, max_players):

        players = 0

        while(players == 0):
            players = self.controller.choose_from([1, 2, 3, 4, 5, 6, 7, 8], 'How many players do you want?')

        return players

    def get_name(self):
        
        return self.controller.get_confirm_input('Enter your name.\n> ', 'Are you okay with this name (y/n)?\n> ')

    def create_players(self):

        total_players = self.get_players(2, 10)
        player_names = []
        players = []

        for i in range (0, total_players):

            print('Player ' + str(i + 1) + ', choose a name')
            
            while(True):
                name = self.get_name()
                if(name in player_names):
                    print('That name has already been taken. Please choose another name.')
                else:
                    break
                
            player_names.append(name)
            os.system('clear')


        random.shuffle(player_names)

        start_gold = 2

        for player in player_names:
            players.append(Player(player, start_gold))
            start_gold += 1
        
        return players

    
    def take_turn(self, player, players):
        self.controller.wait_input('It is ' + player.name + '\'s turn. [ENTER]')
        os.system('clear')
        
        ans = None
        while(ans != 'Take turn'):
            ans = self.controller.choose_from(['View self', 'View other players', 'View scrapyard', 'Take turn'])
            if(ans == 'View self'):
                print('Gold: ' + str(player.gold))
                player.robot.display_robot()
                self.controller.wait_input()
            elif(ans == 'View other players'):
                players = players[:]
                players.remove(player)
                player_names = []
                for user in players:
                    player_names.append(user.name)
                
                ans = self.controller.choose_from(player_names)
                
                for user in players:
                    if(user.name == ans):
                        print('Gold for ' + ans + ': ' + str(user.gold))
                        user.robot.display_robot()
                        break
                self.controller.wait_input()
            elif(ans == 'View scrapyard'):
                print(self.scrapyard)
                self.controller.wait_input()

        player.take_turn(self.scrapyard, self.deck)
        os.system('clear')

        # list items with abilities / abilities, choose/use abilities

        self.controller.wait_input(player.name + '\'s turn is over [ENTER]')
        os.system('clear')

    def gamestate(self):
        for player in self.players:
            if(player.robot.check_won()):
                print(player.name + ' won!')
                break
            else:
                self.take_turn(player, self.players)
                self.gamestate()

    def start(self):
        self.gamestate()