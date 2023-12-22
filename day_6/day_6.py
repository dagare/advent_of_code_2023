class Game:
    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance


game_results = []
file = open("day_6/day_6_input_1.txt", "r")


time_line = ""
distance_line = ""

for line in file:
    split_result = line.split(':')

    
    numbers = split_result[1].split(' ')
    numbers = [int(x) for x in numbers if x]


    if time_line == "":
        time_line = numbers
    else:
        distance_line = numbers
        break

games = []
for i in range(len(time_line)):
    games.append(Game(time_line[i], distance_line[i]))

print(f'Games: {len(games)}')

multiplied_sum = 1
for game in games:
    local_sum = 0

    # get local gum
    for wait_time in range(game.time+1):
        boat_speed = wait_time * 1

        # can win..
        raced_distance = boat_speed * (game.time - wait_time)
        wait_time_is_win = raced_distance > game.distance 
        
        if wait_time_is_win:
            local_sum += 1

        #print(f'game:{game.time}, wait_time:{wait_time}, boat_speed:{boat_speed}, wait_time_is_win:{wait_time_is_win}, raced_distance:{raced_distance}')

    print(f'Game:{game.time} multiplied_sum:{multiplied_sum} local_sum:{local_sum}')   
    multiplied_sum = multiplied_sum * local_sum


print(f'Multiplied_sum: {multiplied_sum}')