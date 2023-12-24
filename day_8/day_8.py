

class LeftRightSequence:
    def __init__(self, line: str):
        self.raw_path = line
        

        self.path_array = []

        for char in line:
            if char == 'L':
                self.path_array.append(True)
            elif char == 'R':
                self.path_array.append(False)

    def get_direction(self, index_counter: int) -> bool:
        mod_index = index_counter % len(self.path_array)

        direction = self.path_array[mod_index]
        #print(f'index_counter:{index_counter}\t mod_index:{mod_index}\t direction:{direction}')

        return direction



class Island:
    def __init__(self, line: str):
        line = line.replace(" ", "")
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("\n", "")

        split_result = line.split('=')

        self.name = split_result[0]
        
        split_result = split_result[1].split(',')

        self.left = split_result[0]
        self.right = split_result[1]

#def find_next_island(left_right_sequence: LeftRightSequence, islands: [Island], jump_counter: int, current_island: Island):
def find_next_island_name(jump_counter: int, current_island_name: str):
    if left_right_sequence.get_direction(jump_counter):
        # Go left
        return islands[current_island_name].left
    
    return islands[current_island_name].right


file = open("day_8/input.txt", "r")
#file = open("day_8/simple_input.txt", "r")

left_right_sequence = 0
islands = dict()
#hand_values = []
i = 1
for line in file:

    if i == 1:
        left_right_sequence = LeftRightSequence(line)
    elif i > 2:
        island = Island(line)
    
        islands[island.name] = island

    i += 1


print(f'LeftRightSequence:{left_right_sequence.raw_path}')

found_zzz = False
jump_counter = 0
next_island_name = 'AAA'
while not found_zzz:
    #next_island = find_next_island(left_right_sequence, islands, jump_counter, next_island)
    next_island_name = find_next_island_name(jump_counter, next_island_name)

    jump_counter += 1
    
    if next_island_name == 'ZZZ':
        found_zzz = True
        print(f'Found ZZZ after jumps: {jump_counter}')
    