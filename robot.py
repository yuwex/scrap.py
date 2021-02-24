from part import Part

class Robot:
    def __init__(self):
        self.parts = {'head' : [], 'arm' : [], 'leg' : [], 'shell' : [], 'cell' : [], 'extra' : [], 'weapon' : [], 'forge' : [], 'discard' : []}

    def __str__(self):
        return str(self.parts)
    
    def get_robot(self):
        return self.parts


    def check_location(self, location):
        # Returns self.parts[location] if true, false if false
        if len(self.parts[location]) < 0 or (len(self.parts[location]) < 1 and location in ['arm', 'leg']):
            return self.parts[location]
        return False

    def add_part(self, part, location):
        self.parts[location].append(part)

    def move_part(self, part, loc1, loc2):
        self.parts[loc1].remove(part)
        self.parts[loc2].append(part)
    
    def find_part(self, part):
        robot_parts = self.get_robot()
        robot_types = list(robot_parts)

        for part_type in robot_types:
            i = 0
            for current_part in robot_parts[part_type]:
                if(current_part == part):
                    return [part_type, i]
                i += 1
        return None

    def find_flaws(self):
        robot_parts = self.parts.copy()
        del robot_parts['forge']
        del robot_parts['discard']
        robot_types = list(robot_parts)
        found_parts = []
        for part_type in robot_types:
            for part in robot_parts[part_type]:
                if(part.flaw > 0):
                    found_parts.append(part)
        
        return found_parts

    def check_won(self):
        all_parts = self.parts.copy()
        bad_key = ['extra', 'weapon', 'forge', 'discard']
        [all_parts.pop(key) for key in bad_key]
        all_keys = all_parts.keys()

        completed = True
        for key in all_keys:
            if((key == 'leg' or key == 'arm') and len(all_parts[key]) != 2):
                completed = False
                break
            elif(len(all_parts[key]) < 1):
                completed = False
                break
        
        return completed
    
    def get_all_parts(self):
        robot_parts = self.parts.copy()
        del robot_parts['forge']
        del robot_parts['discard']
        robot_types = list(robot_parts)

        found_parts = []
        for part_type in robot_types:
            for part in robot_parts[part_type]:
                    found_parts.append(part)
        
        return found_parts


