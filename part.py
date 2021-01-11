class Part:
    def __init__(self, name="", flaw=0, gold=0, type="", ability_text="None", ability_id=0, conditions=False):
        self.name = name
        self.maxflaw = flaw
        self.flaw = flaw
        self.gold = gold
        self.type = type
        self.ability_text = ability_text
        self.ability_id = ability_id

    def add_flaw(self, num=1):
        if(type(num) is int and num > 0):
            self.flaw += num

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
