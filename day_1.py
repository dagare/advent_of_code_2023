
import re

sum = 0

file = open("day_1_input.txt", "r")
for line in file:
    integers = map(int, re.findall(r'\d', line))
    print(f'{line} -> {integers}')

    integers = list(integers)

    if (len(integers)):
        first_element = integers[0]
        last_element = integers[-1]
        
        print(f'first_element: {first_element} \t last_element: {last_element}')


        sum += first_element * 10 + last_element



print(f'part 1 sum is: {sum}')



def convert_to_integer(input_string):
    if (input_string.isdigit()):
        return int(input_string)
    elif (input_string == "one"):
        return 1
    elif (input_string == "two"):
        return 2
    elif (input_string == "three"):
        return 3
    elif (input_string == "four"):
        return 4
    elif (input_string == "five"):
        return 5
    elif (input_string == "six"):
        return 6
    elif (input_string == "seven"):
        return 7
    elif (input_string == "eight"):
        return 8
    elif (input_string == "nine"):
        return 9
    
    return 1000000000



def find_value_of_first_and_last_digit_or_word(input_string):
    # Define a pattern to match any digit (0-9) or its corresponding word
    #pattern = re.compile(r'\\b(?:zero|one|two|three|four|five|six|seven|eight|nine|\\d)\\b', re.IGNORECASE)

    pattern = re.compile(r'(?:one|two|three|four|five|six|seven|eight|nine|[1-9])', re.IGNORECASE)

    # Find all matches in the string
    matches = pattern.findall(input_string)

    matches_r2l = []
    for i in range(len(input_string), 0, -1):
        substring = input_string[-i:]
        matches_r2l += pattern.findall(substring)

    if matches:
        # Get the first match
        first_match = convert_to_integer(matches[0])
        last_match = convert_to_integer(matches_r2l[-1])

        result = first_match * 10 + last_match

        print(f'line:{input_string} -> first:{first_match}\t last_match:{last_match}\t result:{result}')

        return result
    else:
        print(f'line:{input_string} -> gives:0')

        return 0
    
sum2 = 0

file = open("day_1_input.txt", "r")
for line in file:

    sum2 += find_value_of_first_and_last_digit_or_word(line.lower())
    print(f'sum2:{sum2}')


print(f'part 2 sum is: {sum2}')
