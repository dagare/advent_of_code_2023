
import re

def find_red(line):
    pattern = re.compile(r'\d+(?:/\d+)?(?=\s?red?\b)', re.IGNORECASE)

    # Find all matches in the string
    matches = pattern.findall(line)

    if (matches):
        return int(matches[0])
    return 0


def find_blue(line):
    pattern = re.compile(r'\d+(?:/\d+)?(?=\s?blue?\b)', re.IGNORECASE)

    # Find all matches in the string
    matches = pattern.findall(line)

    if (matches):
        return int(matches[0])
    return 0


def find_green(line):
    pattern = re.compile(r'\d+(?:/\d+)?(?=\s?green?\b)', re.IGNORECASE)

    # Find all matches in the string
    matches = pattern.findall(line)

    if (matches):
        return int(matches[0])
    return 0


def find_game_number(line):
    pattern = re.compile(r'\bGame\s(\d+)\b', re.IGNORECASE)

    # Find all matches in the string
    matches = pattern.findall(line)

    if (matches):
        #split = matches[0].split(" ")

        #return int(split[1])
        return int(matches[0])
    return 0



def parse_and_evaluate_line(line):
    game_number = 0

    #split_result = line.split(';:')
    split_result = re.split(r'[;:]', line)

    game_number = find_game_number(split_result[0])

    print(f'Game number: {game_number}')

    all_ok = True

    for draw in split_result[1:]:
        red = find_red(draw)
        green = find_green(draw)
        blue = find_blue(draw)
        print(f'red:{red}\tgreen:{green}\tblue:{blue}')

        if red > 12 or green > 13 or blue > 14:
            all_ok = False

    print(f'Game number: {game_number} : all_ok:{all_ok}')

    if all_ok:
        return game_number
    
    return 0


def parse_and_evaluate_line_2(line):
    game_number = 0

    #split_result = line.split(';:')
    split_result = re.split(r'[;:]', line)

    game_number = find_game_number(split_result[0])

    print(f'Game number: {game_number}')

    all_ok = True

    min_red = 0
    min_green = 0
    min_blue = 0


    for draw in split_result[1:]:
        red = find_red(draw)
        green = find_green(draw)
        blue = find_blue(draw)
        print(f'red:{red}\tgreen:{green}\tblue:{blue}')

        if red > min_red:
            min_red = red
        if green > min_green:
            min_green = green
        if blue > min_blue:
            min_blue = blue

    power = min_red * min_green * min_blue

    print(f'Game number: {game_number} : minimum red:{min_red}\tgreen:{min_green}\tblue:{min_blue}\tpowers:{power}')

    return power

sum = 0

file = open("day_2_input.txt", "r")
for line in file:

    sum += parse_and_evaluate_line(line)
    print(f'sum:{sum}')


print(f'part 1 sum is: {sum}')


sum_part_2 = 0
file = open("day_2_input.txt", "r")
for line in file:

    sum_part_2 += parse_and_evaluate_line_2(line)
    print(f'sum:{sum_part_2}')


print(f'part 2 sum is: {sum_part_2}')