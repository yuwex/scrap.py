from part import Part
import os
import random

class Controller:

    def choose_from(self, item_list, text='Which item do you choose?', end='\n> '):
        
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
                    ans = item_list[ans-1]
                else:
                    ans = False
            except:
                print('Bad Input')
                ans = False

            if(ans):
                break
        
        return ans

    def wait_input(self, text='[ENTER]'):
        input(text)
    
    def get_confirm_input(self, text, confirm_text='Is this answer ok? (y / n)'):
        confirm = ''
        while not confirm.lower() == 'y':
            ans = input(text)
            confirm = input(confirm_text)
        return ans

    
    