from part import Part
from player import Player
from robot import Robot
from deck import Deck
from scrapyard import Scrapyard

class AbilityManager:
    def __init__(self, deck, scrapyard):
        self.deck = deck
        self.scrapyard = scrapyard
    def __str__(self):
        pass

    def do_ability(self, player, part):
        ID = part.ability_id
        
        if(ID == 1):
            #Collectorarm
            ans = player.robot.choose_from(player.robot.get_all_parts(), 'Which item do you want to forge?')
            print(player.robot.find_part(ans))
            player.robot.move_part(ans, player.robot.find_part(ans)[0], 'forge')
            
            flaw_part = player.robot.find_flaw()
            for part in flaw_part:
                part.remove_flaw(2)
        
        if(ID == 2):
            #Luxury Limb
            player.gold += 2
        
        if(ID == 3):
            #Venitor Arm
            if(player.gold == 0):
                flaw_part = player.robot.find_flaw()
                for part in flaw_part:
                    part.remove_flaw(1)
        
        if(ID == 4):
            #Inc Corp
            top_card = self.deck.get_top()
            top_card.display()
            input('[ENTER]')
            if(player.robot.choose_from(['Yes', 'No'], 'Would you like to obtain this part?') == 'Yes'):
                self.scrapyard.take_part(player, top_card)
        


"""
player = Player('Huckleberry Freindmndednd', 2000000)

#Part(name="", flaw=0, gold=0, pType="", ability_text="None", ability_id=0, conditions=False)
#p1 = Part('naem', 1, 1, 'head', 'dosmthn', 1)
p1 = Part('Joe [Level 300]', 12, 5, 'head', 'laser beams!!!', 1)
p2 = Part('Moe [Level 300]', 3, 5, 'leg', '2 uea!!!', 0)
p3 = Part('Soe [Level YUWEBEATS]', 400, 12, 'leg', 'U10UH <-- new yuwebeats song', 0)
p4 = Part('CodeBreaker', 2, 22, 'arm', 'e4.txt ami.righ.t ;)', 0)
p5 = Part('Banana.', 4, 22, 'arm', 'nanananahnahnahnananana', 0)
p6 = Part('stuck in a ', 101, 101, 'cell', 'nirvana', 0)
p7 = Part('Luv (sic) pt. 7', 0, 2, 'shell', 'love is kind but its also blind', 0)


deck = Deck()


scrapyard = Scrapyard()
robot = Robot()
scrapyard.add_deck(deck, 4)

robot.add_part(p1)
robot.add_part(p2)
robot.add_part(p3)
robot.add_part(p4)
robot.add_part(p5)
robot.add_part(p6)
robot.add_part(p7)

player.robot = robot

#FOR TESTING ADD Deck AND Scrapyard

abilities = AbilityManager(deck, scrapyard)
abilities.do_ability(player, p1)

print(player.robot.display_robot())
"""