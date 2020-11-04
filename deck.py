from part import Part
import random

class Deck:
    def __init__(self, file='parts.csv'):
        self.cards = []
        
        fin = open('parts.csv', 'r')
        fin.readline()
        for line in fin:
            line = line.strip().split(',', 4)
            #print(line)
            if(len(line) == 5):
                self.cards.append(Part(line[0], int(line[1]), int(line[2]), line[3], line[4]))
            else:
                self.cards.append(Part(line[0], int(line[1]), int(line[2]), line[3]))
        fin.close()

    def __str__(self):
        text = ''

        for i in range(0, len(self.cards)):
            text += str(i + 1) + ': ' + str(self.cards[i]) + '\n'
        
        return text

    def take_card(self, num=1):
        num = num
        if(num > len(self.cards)):
            return 'Error: Out of Bounds'
        
        cards_taken = self.cards[:num]
        self.cards = self.cards[num:]
        
        return cards_taken
    
    def shuffle(self):
        random.shuffle(self.cards)

    def replace_top(self, card):
        self.cards[0] = card

    def get_top(self):
        return self.cards[0]