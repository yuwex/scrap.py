class Part:
    def __init__(self, name="", flaw=0, gold=0, pType="", ability_text="None", ability_id=0, conditions=False):
        self.name = name
        self.maxflaw = flaw
        self.flaw = flaw
        self.gold = gold
        self.type = pType
        self.ability_text = ability_text
        self.ability_id = ability_id

    def __str__(self):
        
        return ('name: ' + self.name + ', staring flaws: ' + str(self.maxflaw) + ', flaws: ' + str(self.flaw) + ', gold: ' + str(self.gold) + ', type: ' + self.type + ', ability_text: ' + self.ability_text + ', ability_id: ' + str(self.ability_id))

    def display(self, inscrap=False, indent=0):
        indent = indent * ' '
        text = ''
        text += indent + 'Name: ' + self.name + '\n'
        text += indent + 'Gold: ' + str(self.gold) + ', Starting Flaws: ' + str(self.maxflaw) + '\n'
        text += indent + 'Card Type: ' + self.type + '\n'
        text += indent + 'Ability: ' + self.ability_text + '\n'
        if(not inscrap):
            text += indent + 'Current Flaws: ' + str(self.flaw) + '\n'
            #text += indent + 'Ability Used: ' + str(self.flaw) 
        
        return text

    def add_flaw(self, num=1):
        if(type(num) is int and num > 0):
            self.flaw += num
        else:
            print(type(num))

    def remove_flaw(self, num=1):
        if(type(num) is int and num > 0):
            if(num >= self.flaw):
                self.flaw = 0
            else:
                self.flaw -= num
        elif(num == 0):
            self.flaw = 0
    
    def get_type(self):
        return self.type

    def get_flaw(self):
        return self.flaw
    
    def get_gold(self):
        return self.gold

    def get_name(self):
        return self.name


# coolpart = Part(name='joe')
# print(coolpart)
# coolpart.add_flaw()
# print(coolpart)