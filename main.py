from part import Part
from player import Player
from robot import Robot
from scrapyard import Scrapyard
from deck import Deck

import random
import os


def get_players(min_players, max_players):

    players = 0

    while(players == 0):
        players = input('How many players do you want?\n> ')
        try:
            players = int(players)
        except:
            players = 0
        
        if(players < min_players or players > max_players):
            players = 0
            print('There must be between ' + str(min_players) + ' and ' + str(max_players) + ' players.')

    return players

def get_name():

    while(True):
        name = input('Enter your name.\n> ')
        if(input('Are you okay with this name (y/n)?\n> ') == 'y'):
            break
    return name

def create_players():

    total_players = get_players(2, 10)
    player_names = []
    players = []

    for i in range (0, total_players):

        print('Player ' + str(i + 1) + ', choose a name')
        
        while(True):
            name = get_name()
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

def take_turn(player, players):
    input('It is ' + player.name + '\'s turn. [ENTER]\n> ')
    os.system('clear')
    
    ans = None
    while(ans != 'Take turn'):
        ans = player.robot.choose_from(['View self', 'View other players', 'View scrapyard', 'Take turn'])
        if(ans == 'View self'):
            print('Gold: ' + str(player.gold))
            player.robot.display_robot()
            input('[ENTER]\n> ')
        elif(ans == 'View other players'):
            players = players[:]
            players.remove(player)
            player_names = []
            for user in players:
                player_names.append(user.name)
            
            ans = player.robot.choose_from(player_names)
            
            for user in players:
                if(user.name == ans):
                    print('Gold for ' + ans + ': ' + str(user.gold))
                    user.robot.display_robot()
                    break
            input('[ENTER]\n> ')
        elif(ans == 'View scrapyard'):
            print(scrapyard)
            input('[ENTER]\n> ')

    player.take_turn(scrapyard, deck)
    os.system('clear')

    # list items with abilities / abilities, choose/use abilities

    input(player.name + '\'s turn is over [ENTER]\n> ')
    os.system('clear')

#Set up variables
os.system('clear')

players = create_players()
deck = Deck()
deck.shuffle()

#part = Part('rich mint-condition cat head', 0, 100, 'head', 'mew mew may the gods bless you')
#deck.replace_top(part)

scrapyard = Scrapyard()
scrapyard.add_deck(deck, 4)

# NOTE
# Take turn can only be called AFTER a scrapyard variable is created.
while(True):
    for player in players:
        if(player.robot.check_won()):
            print(player.name + ' won!')
            break
        else:
            take_turn(player, players)

