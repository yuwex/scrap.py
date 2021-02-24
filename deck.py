from part import Part
import random
import os

class Deck:
    def __init__(self, file='parts.csv'):
        random.seed(100)
        self.parts = []
        
        # os.chdir('Scrapyard-Git/scrap.py')
        fin = open('parts.csv', 'r')
        fin.readline()
        for line in fin:
            line = line.strip().split(',', 4)
            #print(line)
            if(len(line) == 5):
                self.parts.append(Part(line[0], int(line[1]), int(line[2]), line[3], line[4]))
            else:
                self.parts.append(Part(line[0], int(line[1]), int(line[2]), line[3]))
        fin.close()

    def __str__(self):
        text = ''

        for i in range(0, len(self.parts)):
            text += str(i + 1) + ': ' + str(self.parts[i]) + '\n'
        
        return text

    def take_card(self, num=1):
        num = num
        if(num > len(self.parts)):
            return 'Error: Out of Bounds'
        
        cards_taken = self.parts[:num]
        self.parts = self.parts[num:]
        
        return cards_taken
    
    def shuffle(self):
        random.shuffle(self.parts)

    def replace_top(self, card):
        self.parts[0] = card

    def get_top(self):
        return self.parts[0]