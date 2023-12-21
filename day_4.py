import re

def parse_and_evaluate_line(line, return_exual_count=False):
    split_result = line.split(':')

    split_result_2 = split_result[1].split('|')

    winning_numbers = split_result_2[0].split(" ")
    winning_numbers = [int(x) for x in winning_numbers if x]
    my_numbers = split_result_2[1].split(" ")
    my_numbers = [int(x) for x in my_numbers if x]

    print(f'winning_numbers:{winning_numbers} \t my_numbers:{my_numbers}')

    equal_count = 0
    result = 0

    for my_number in my_numbers:
        if my_number in winning_numbers:
            equal_count += 1


    print(f'line:{line} equal_count:{equal_count} result:{2**(equal_count-1)}')

    if return_exual_count:
        return equal_count

    if (equal_count <= 0):
        return 0
    
    return 2**(equal_count-1)

scores = []
file = open("day_4_input_simple.txt", "r")
for line in file:

    scores.append(parse_and_evaluate_line(line))

print(f'sum:{sum(scores)}')

file = open("day_4_input.txt", "r")
proper_scores = []
for line in file:

    proper_scores.append(parse_and_evaluate_line(line))

print(f'sum part 1: {sum(proper_scores)}')


game_results = []
file = open("day_4_input_simple.txt", "r")
for line in file:
    game_results.append(parse_and_evaluate_line(line, True))


cards_per_game = [0]*len(game_results)
for i in range(len(game_results)):
    # Add Original
    cards_per_game[i] += 1

    # Many other cards might have been added previously


    for j in range(i+1, i+game_results[i]+1):
        cards_per_game[j] += cards_per_game[i] 
    
    
for cards in cards_per_game:
    print(f'cards:{cards}')

print(f'sum of cards_per_game:{sum(cards_per_game)}')