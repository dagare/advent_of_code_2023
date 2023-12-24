from enum import Enum

class HandType(Enum):
    FIVE__ = 100
    FOUR__ = 90
    HOUSE_ = 80
    THREE_ = 70 
    PAIRx2 = 60
    PAIRx1 = 50
    HIGH_C = 40   
    
def char_to_value(card_char: str):
    if card_char == 'J':
        return 1
    elif card_char.isdigit():
        if int(card_char) <= 1:
            print(f'Wrong value when parsing hand. card_char:{card_char} -> int:{int(card_char)})')
        return int(card_char)
    elif card_char == 'T':
        return 10
    elif card_char == 'Q':
        return 11
    elif card_char == 'K':
        return 12
    elif card_char == 'A':
        return 13

def first_higher_than_second(first_hand: str, second_hand: str) -> bool:
    for i in range(len(first_hand)):
        if char_to_value(first_hand[i]) > char_to_value(second_hand[i]):
            return True
        if char_to_value(first_hand[i]) < char_to_value(second_hand[i]):
            return False
        
    #print(f'first({first}) is equal to second({second})')
    return False

class Hand:
    def __init__(self, line_input: str):
        split_result = line_input.split(' ')

        self.cards = split_result[0]
        
        self.bid = int(split_result[1])

        self.card_values = []
        card_hex_values = "0x"
        # Convert card values to numeric values
        for card_char in self.cards:
            if card_char == 'J':
                self.card_values.append(1)
                card_hex_values+='1'
            elif card_char.isdigit():
                if int(card_char) <= 1:
                    print(f'Wrong value when parsing hand. card_char:{card_char} -> int:{int(card_char)})')
                self.card_values.append(int(card_char))
                card_hex_values+=card_char
            elif card_char == 'T':
                self.card_values.append(10)
                card_hex_values+='A'
            elif card_char == 'Q':
                self.card_values.append(11)
                card_hex_values+='B'
            elif card_char == 'K':
                self.card_values.append(12)
                card_hex_values+='C'
            elif card_char == 'A':
                self.card_values.append(13)
                card_hex_values+='D'
            else:
                print(f'illegal char when parsing hand: {card_char}')
        
        self.hand_value = int(card_hex_values, 16)
        #print(f'{self.cards} evaluates to {self.card_values} -> ({self.hand_value})')

        #cards_copy = self.cards
        no_jokers = create_a_stronger_hand_using_jokers(self.cards)
        unique_cards = list(dict.fromkeys(no_jokers))
        print(f'self.cards:{self.cards}\t no_jokers:{no_jokers}\t unique_cards:{unique_cards}')
        #unique_cards = list(dict.fromkeys(cards_copy))

        if len(unique_cards) == 1:
            self.hand_type = HandType.FIVE__
        elif len(unique_cards) == 2:
            if no_jokers.count(unique_cards[0]) == 4 or no_jokers.count(unique_cards[1]) == 4:
                self.hand_type = HandType.FOUR__
            else:
                self.hand_type = HandType.HOUSE_
        elif len(unique_cards) == 3:
            if no_jokers.count(unique_cards[0]) == 3 or no_jokers.count(unique_cards[1]) == 3 or no_jokers.count(unique_cards[2]) == 3:
                self.hand_type = HandType.THREE_
            else:
                self.hand_type = HandType.PAIRx2
        elif len(unique_cards) == 4:
            self.hand_type = HandType.PAIRx1
        elif len(unique_cards) == 5:
            self.hand_type = HandType.HIGH_C
        else: 
            print(f'Invalud hand type!!!')
        


        
        print(f'hand:{self.cards}\tunique_cards:{unique_cards} -> hand_type:{self.hand_type}')

    def set_hand_rank(self, rating: int):
        self.hand_rank = rating

        
def create_a_stronger_hand_using_jokers(cards):
    unique_cards = list(dict.fromkeys(cards))

    if not 'J' in unique_cards:
        print(f'cards:{cards} does not contain any Jokers')
        return cards
    if len(unique_cards) == 1 and unique_cards[0] == 'J':
        return cards
    
    max_char = find_max_char(cards)



    new_string = cards.replace('J', max_char)

    print(f'card:{cards} -> new_string:{new_string}')
    return new_string
    

def find_number_of_jokers(cerds):
    # Create an empty dictionary to store character counts
    char_count = {}

    # Count occurrences of each character
    for char in cerds:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the number of occurrences of 'J'
    return char_count.get('J', 0)

def find_max_char(cards):
    # Create an empty dictionary to store character counts
    char_count = {}

    # Count occurrences of each character
    for char in cards:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the character with the highest count
    #max_char = max(char_count, key=char_count.get)
    #max_count = char_count[max_char]

    # Exclude 'J' from the dictionary
    char_count_without_J = {k: v for k, v in char_count.items() if k != 'J'}

    # Find characters with the highest count (excluding 'J')
    max_count = max(char_count_without_J.values(), default=0)

    max_chars = [char for char, count in char_count_without_J.items() if count == max_count]
    print(f"Character counts (excluding 'J'): {char_count_without_J}")
    print(f"Characters with the highest count (excluding 'J'): {max_chars} (count: {max_count})")

    if 'A' in max_chars:
        return 'A'
    elif 'K' in max_chars:
        return 'K'
    elif 'Q' in max_chars:
        return 'Q'
    elif 'T' in max_chars:
        return 'T'
    elif '9' in max_chars:
        return '9'
    elif '8' in max_chars:
        return '8'
    elif '7' in max_chars:
        return '7'
    elif '6' in max_chars:
        return '6'
    elif '5' in max_chars:
        return '5'
    elif '4' in max_chars:
        return '4'
    elif '3' in max_chars:
        return '3'
    elif '2' in max_chars:
        return '2'
    else: # 'J'
        print(f'max_chars:{max_chars}. returning J')
        return 'J'

    #max_char = max(char_count_without_J, key=char_count_without_J.get)
    #max_count = char_count_without_J[max_char]
    
    # Print the results
    print(f"cards:{cards}\tCharacter counts: {char_count}\tCharacter with the highest count: '{max_char}' (count: {max_count})")

    return None

file = open("day_7/day_7_input.txt", "r")
#file = open("day_7/day_7_input_simple.txt", "r")
#file = open("day_7/dey_7_debug.txt", "r")

hands = []
#hand_values = []
i = 1
for line in file:
    print(f'parsers counter i:{i}')
    hands.append(Hand(line))
    #hands[-1].hand_value
    i += 1

#hand_values.sort()


rating_counter = 1

for i in range(len(hands)):

    #print(f'\ni:{i}, hand_type:{hands[i].hand_type}({hands[i].hand_type.value})\t hand_value:{hands[i].hand_value} \tcards:{hands[i].cards}')
    better_count = 1
    worse_count = 1
    for j in range(len(hands)):
        if (i != j):
            debug_line = f'j:{j}, hand_type:{hands[j].hand_type.value}\t hand_value:{hands[j].hand_value}'

            # How many are better?
            if hands[i].hand_type.value > hands[j].hand_type.value:
                better_count += 1
                debug_line += f'\ti < j. \tbetter_count:{better_count} \tworse_count_count:{worse_count}'
            elif hands[i].hand_type == hands[j].hand_type:
                
                
                #if hands[i].hand_value > hands[j].hand_value:
                if first_higher_than_second(hands[i].cards, hands[j].cards):
                    better_count += 1
                    debug_line += f'\ti == j, i < j. \tbetter_count:{better_count} \tworse_count_count:{worse_count}' 
                else: 
                    worse_count += 1
                    debug_line += f'\ti == j, else. \tbetter_count:{better_count} \tworse_count_count:{worse_count}'
            else:
                worse_count += 1
                debug_line += f'\ti < j (else) \tbetter_count:{better_count} \tworse_count_count:{worse_count}'

            #print(debug_line)

    hands[i].set_hand_rank(len(hands) + 1 - worse_count)


accumulate_values = 0   
hand_ranks = []
for hand in hands:
    #print(f'hand:{hand.cards}({hand.hand_type}). bid:{hand.bid}\tvalue:{hand.hand_value}.\thand_rank:{hand.hand_rank}')
    hand_ranks.append(hand.hand_rank)
    accumulate_values += hand.bid * hand.hand_rank

print(f'Win value: {accumulate_values}')


list_set = set(hand_ranks)
# convert the set to the list
unique_list = (list(list_set))

print(f'hand_ranks unique_count:{len(unique_list)} (and original length:{len(hand_ranks)}) (min:{min(hand_ranks)}, max:{max(hand_ranks)})')

for i in range(max(hand_ranks)+1):
    for hand in hands:
        if hand.hand_rank == i:
            #print(f'hand:{hand.cards}({hand.hand_type}). bid:{hand.bid}\tvalue:{hand.hand_value}.\thand_rank:{hand.hand_rank}')
            print(f'{hand.hand_rank}\t{hand.cards}\t{hand.bid}')
            j = 1
