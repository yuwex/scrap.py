from part import Part
from controller import Controller

class Robot:
    def __init__(self):
        self.parts = {'head' : [], 'arm' : [], 'leg' : [], 'shell' : [], 'cell' : [], 'extra' : [], 'weapon' : [], 'forge' : [], 'discard' : []}
        self.controller = Controller()

    def __str__(self):
        return str(self.parts)
    
    def get_parts(self):
        return self.parts

    def add_part(self, part):

        part_type = part.get_type()
        location_go = part_type
        
        if part_type in self.parts.keys():
            if((part_type in ['arm', 'leg'] and len(self.parts[part_type]) > 1) or (part_type not in ['arm', 'leg'] and len(self.parts[part_type]) > 0)):
                
                if(len(self.parts['extra']) > 0):
                    parts_list = self.parts[part_type]
                    parts_list.append(self.parts['extra'][0])

                    forge_part = self.controller.choose_from(parts_list, 'Choose a part to forge. #3 is your extra slot item')
                    self.move_part(forge_part, part_type, 'forge')
                    if(len(self.parts['extra']) == 0):
                        location_go = 'extra'
                    
                else:
                    
                    location_go = 'extra'

            self.parts[location_go].append(part)
            self.controller.wait_input('Your part has been moved to the ' + location_go + ' slot [ENTER]')

        else:

            print('Fatal Error: Not in Keys')
            print('\nInputs: \nPart:', end = ' ')
            print(str(part))
            exit()

    def move_part(self, part, loc1, loc2):
        self.parts[loc1].remove(part)
        self.parts[loc2].append(part)
        
    def display_robot(self):
        print('-'*10)
        for key in self.parts.keys():
            print(key + ':')
            if(not len(self.parts[key]) == 0):
                #print(end='\t')
                for part in self.parts[key]:
                    print(part.display(indent=4))
                print()
        print('-'*10)
    
    def remove_flaws(self, flaws=2, different=False, skip=False):
        
        flaw_parts = self.find_flaw()

        for i in range (flaws):

            i = i
            if(len(flaw_parts) == 0):
                print('There were no removable flaws')
                break
            if(skip):
                ans = self.controller.choose_from(flaw_parts + ['Skip'], 'Choose a part to remove 1 flaw from.')
            else:
                ans = self.controller.choose_from(flaw_parts, 'Choose a part to remove 1 flaw from.')

            location = self.find_part(ans)
            if(location):
                self.parts[location[0]][location[1]].remove_flaw()
                if(different):
                    flaw_parts.remove(ans)
                elif(self.parts[location[0]][location[1]].flaw == 0):
                    flaw_parts.remove(ans)
            else:
                print('You skipped removing flaws')
                break
        
    def find_part(self, part):
        robot_parts = self.get_parts()
        robot_types = list(robot_parts)

        for part_type in robot_types:
            i = 0
            for current_part in robot_parts[part_type]:
                if(current_part == part):
                    return [part_type, i]
                i += 1
        return None

    def find_flaw(self):
        
        robot_parts = self.parts.copy()
        del robot_parts['forge']
        del robot_parts['discard']
        robot_types = list(robot_parts)

        #creates found_parts list w/ all parts with >0 flaws
        found_parts = []
        #found_parts_location = []
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

        #creates found_parts list
        found_parts = []
        #found_parts_location = []
        for part_type in robot_types:
            for part in robot_parts[part_type]:
                    found_parts.append(part)
        
        return found_parts

# cards = []
# fin = open('parts.csv', 'r')
# for line in fin:
#     line = line.strip().split(',', 4)
#     if(len(line) == 5):
#         cards.append(Part(line[0], line[1], line[2], line[3], line[4]))
#     else:
#         cards.append(Part(line[0], line[1], line[2], line[3]))
# fin.close()



# p1 = Part('Joe [Level 300]', 12, 5, 'head', 'laser beams!!!', {'passive': 'kill all other'})
# p2 = Part('Moe [Level 300]', 3, 5, 'leg', '2 uea!!!', {'passive': 'memer'})
# p3 = Part('Soe [Level YUWEBEATS]', 400, 12, 'leg', 'U10UH <-- new yuwebeats song')
# p4 = Part('CodeBreaker', 2, 22, 'arm', 'e4.txt ami.righ.t ;)')
# p5 = Part('Banana.', 4, 22, 'arm', 'nanananahnahnahnananana')
# p6 = Part('stuck in a cell', 101, 101, 'cell', 'nirvana', {'passive': 'prague'})
# p7 = Part('Luv (sic) pt. 7', 0, 2, 'shell', 'love is kind but its also blind', {'passive': 'luvsick like a doge canine sensetivity'})



# robot = Robot()

# robot.add_part(p1)
# robot.add_part(p2)
# robot.add_part(p3)
# robot.add_part(p4)
# robot.add_part(p5)
# robot.add_part(p6)
# robot.add_part(p7)


# for part in robot.get_all_parts():
#     print(part)

#robot.check_won()

# robot.remove_flaws(flaws=1, different=False, skip=True)


