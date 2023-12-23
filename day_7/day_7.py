from enum import Enum

class HandType(Enum):
    FIVE_OF_A_KIND = 100
    FOUR_OF_A_KIND = 90
    FULL_HOUSE = 80
    THREE_OF_A_KIND = 70 
    TWO_PAIR = 60
    ONE_PAIR = 50
    HIGH_CARD = 40   
    
def second_higher_than_first(first: [int], second: [int]) -> bool:
    for i in range(len(first)):
        if second[i] > first[i]:
            return True
        if second[i] < first[i]:
            return False
        
    print(f'first({first}) is equal to second({second})')
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
            if card_char.isdigit():
                if int(card_char) <= 1:
                    print(f'Wrong value when parsing hand. card_char:{card_char} -> int:{int(card_char)})')
                self.card_values.append(int(card_char))
                card_hex_values+=card_char
            elif card_char == 'T':
                self.card_values.append(10)
                card_hex_values+='A'
            elif card_char == 'J':
                self.card_values.append(11)
                card_hex_values+='B'
            elif card_char == 'Q':
                self.card_values.append(12)
                card_hex_values+='C'
            elif card_char == 'K':
                self.card_values.append(13)
                card_hex_values+='D'
            elif card_char == 'A':
                self.card_values.append(14)
                card_hex_values+='E'
            else:
                print(f'illegal char when parsing hand: {card_char}')
        
        self.hand_value = int(card_hex_values, 16)
        #print(f'{self.cards} evaluates to {self.card_values} -> ({self.hand_value})')

        #cards_copy = self.cards
        unique_cards = list(dict.fromkeys(self.cards))
        #unique_cards = list(dict.fromkeys(cards_copy))

        if len(unique_cards) == 1:
            self.hand_type = HandType.FIVE_OF_A_KIND
        elif len(unique_cards) == 2:
            if self.cards.count(unique_cards[0]) == 4 or self.cards.count(unique_cards[1]) == 4:
                self.hand_type = HandType.FOUR_OF_A_KIND
            else:
                self.hand_type = HandType.FULL_HOUSE
        elif len(unique_cards) == 3:
            if self.cards.count(unique_cards[0]) == 3 or self.cards.count(unique_cards[1]) == 3 or self.cards.count(unique_cards[2]) == 3:
                self.hand_type = HandType.THREE_OF_A_KIND
            else:
                self.hand_type = HandType.TWO_PAIR
        elif len(unique_cards) == 4:
            self.hand_type = HandType.ONE_PAIR
        elif len(unique_cards) == 5:
            self.hand_type = HandType.HIGH_CARD
        else: 
            print(f'Invalud hand type!!!')
        
        
        #print(f'unique_cards:{unique_cards} -> hand_type:{self.hand_type}')

    def set_hand_rank(self, rating: int):
        self.hand_rank = rating

        
file = open("day_7/day_7_input.txt", "r")

hands = []
#hand_values = []
for line in file:
    hands.append(Hand(line))
    #hands[-1].hand_value

#hand_values.sort()


rating_counter = 1

for i in range(len(hands)):

    print(f'\ni:{i}, hand_type:{hands[i].hand_type.value}\t hand_value:{hands[i].hand_value} \tcards:{hands[i].cards}')
    better_count = 1
    worse_count = 1
    for j in range(1, len(hands)):
        if (i != j):
            debug_line = f'j:{j}, hand_type:{hands[j].hand_type.value}\t hand_value:{hands[j].hand_value}'

            # How many are better?
            if hands[i].hand_type.value > hands[j].hand_type.value:
                better_count += 1
                debug_line += f'\ti < j. \tbetter_count:{better_count} \tworse_count_count:{worse_count}'
            elif hands[i].hand_type == hands[j].hand_type:
                
                
                if hands[i].hand_value > hands[j].hand_value:
                #if second_higher_than_first(hands[i].card_values, hands[j].card_values):
                    better_count += 1
                    debug_line += f'\ti == j, i < j. \tbetter_count:{better_count} \tworse_count_count:{worse_count}' 
                else: 
                    worse_count += 1
                    debug_line += f'\ti == j, else. \tbetter_count:{better_count} \tworse_count_count:{worse_count}'
            else:
                worse_count += 1
                debug_line += f'\ti < j (else) \tbetter_count:{better_count} \tworse_count_count:{worse_count}'

            print(debug_line)

    hands[i].set_hand_rank(len(hands) + 1 - worse_count)


accumulate_values = 0
hand_ranks = []
for hand in hands:
    print(f'hand:{hand.cards}. bid:{hand.bid} value:{hand.hand_value}. global_rating:{hand.hand_rank}')
    hand_ranks.append(hand.hand_rank)
    accumulate_values += hand.bid * hand.hand_rank

print(f'Win value: {accumulate_values}')

list_set = set(hand_ranks)
# convert the set to the list
unique_list = (list(list_set))

print(f'hand_ranks unique_count:{len(unique_list)} (and original length:{len(hand_ranks)}) (min:{min(hand_ranks)}, max:{max(hand_ranks)})')