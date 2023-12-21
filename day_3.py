def create_padded_char_matrix(file_path):
    char_matrix = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                row = list('.' + line.strip() + '.')  # Add padding and convert each line to a list of characters
                char_matrix.append(row)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Add top and bottom padding
    char_matrix.insert(0, ['.' for _ in char_matrix[0]])
    char_matrix.append(['.' for _ in char_matrix[0]])

    return char_matrix

# Print the character matrix
def print_matrix(matrix, name=""):
    print(f'Matrix:{name}')
    for row in matrix:
        print("".join(row))


# Example usage:
file_path = 'day_3_input_simple.txt'  # Replace with the path to your file
result_char_matrix = create_padded_char_matrix(file_path)
print_matrix(result_char_matrix, "result_char_matrix")



def is_part_number(matrix):
    part_numbers = []
    print_matrix(matrix, "is_part_number?_matrix")

    for j in range(0, len(matrix[0]) ):
        char = matrix[0][j]
        if not (char.isdigit() or char == '.'):
            return True
        char = matrix[2][j]
        if not (char.isdigit() or char == '.'):
            return True
    char = matrix[1][0]
    if not (char.isdigit() or char == '.'):
        return True   
    char = matrix[1][len(matrix[1])-1]
    if not (char.isdigit() or char == '.'):
        return True        

    return False

def get_maxtrix_around_number(full_matrix, number_start_j, number_end_j, row_i):
    delta_j = number_end_j-number_start_j
    #print(f'get_maxtrix_around_number start_j:{number_start_j} end_j:{number_end_j} row_i:{row_i} delta_j:{delta_j}')

    a = extract_smaller_matrix(full_matrix, number_start_j-1, number_end_j+2, row_i-1, row_i+2)
    #print_matrix(a, "matrix_around_number")
    return a

def extract_smaller_matrix(matrix, start_col, end_col, start_row, end_row):
    smaller_matrix = [
        row[start_col:end_col] for row in matrix[start_row:end_row]
    ]
    return smaller_matrix


def find_part_numbers(matrix):
    part_numbers = []

    for i in range(1, len(matrix) - 1):

        number_start = 0

        for j in range(1, len(matrix[i])):
            char = matrix[i][j]
            #print(f"Matrix[{i}][{j}]: {char}")

            if (matrix[i][j].isdigit() and number_start<=0):
                number_start = j
            if (not matrix[i][j].isdigit() and number_start>0):
                number_end = j-1
                matrix_around_number = get_maxtrix_around_number(matrix, number_start, number_end, i)

                result_integer = int(''.join(matrix[i][number_start:number_end+1]))

                if (is_part_number(matrix_around_number)):
                    print(f'Adding {result_integer} as a number.')
                    part_numbers.append(result_integer)
                else:
                    print(f'Skipping {result_integer}')
            
                # reset number_start
                number_start = 0


    return part_numbers

def find_int_right_to_left(line, start_index):
    if (not line[start_index].isdigit()):
        return 0
    
    print(f'reversed range:{reversed(range(0, start_index))}')
    
    for j in reversed(range(0, start_index)):
        if (not line[j].isdigit()):

            val = int(''.join(line[j+1:start_index+1]))
            print(f'find_int_right_to_left. j:{j} start_index:{start_index} str:{line[j+1:start_index+1]} val:{val}')
            return val

    print(f'find_int_right_to_left. something weird happened start_index:{start_index}')    
    return 0
        
def find_int_left_to_right(line, start_index):
    if (not line[start_index].isdigit()):
        return 0
    
    for j in range(start_index+1, len(line)):
        if (not line[j].isdigit()):
            number_end = j-1

            val = int(''.join(line[start_index:j]))
            print(f'find_int_left_to_right. j:{j} start_index:{start_index} str:{line[start_index:j]} val:{val}')
            return int(''.join(line[start_index:j]))
        

    print(f'find_int_left_to_right. something weird happened start_index:{start_index}')    

def find_ints(line, center_index):
    # if (not line[center_index-1].isdigit() or
    #     not line[center_index].isdigit() or
    #     not line[center_index+1].isdigit()):
    #     return 0
    
    if (not line[center_index].isdigit()):
        return [
            find_int_right_to_left(line, center_index-1),
            find_int_left_to_right(line, center_index+1)
        ]

    else:
        if (not line[center_index-1].isdigit()):
            return [
                find_int_left_to_right(line, center_index)
            ]
        elif (not line[center_index+1].isdigit()):
            return [
                find_int_right_to_left(line, center_index)
            ]
        else: 
            left = find_int_right_to_left(line, center_index)
            right = find_int_left_to_right(line, center_index+1)
            print(f'left:{left} right:{right}')

            return [
                int(str(left)+str(right))
            ]

def evaluate_and_summerize(numbers):

    number_of_numbers = 0
    posibive_numbers = []
    ratio = 0

    for values in numbers:
        for value in values:
            if (value>0):
                number_of_numbers += 1
                posibive_numbers.append(value)

    if number_of_numbers == 2:
        return posibive_numbers[0] * posibive_numbers[1]
    
    return 0





def find_gear_ratios(matrix):
    gear_ratios = []

    for i in range(1, len(matrix) - 1):


        for j in range(1, len(matrix[i])-1):
            char = matrix[i][j]
            #print(f"Matrix[{i}][{j}]: {char}")

            if (char == '*'):
                # Gear posibility
                print(f'GearPosibility at i:{i} j:{j}')
                numbers = []
                numbers.append([find_int_left_to_right(matrix[i], j+1)])
                numbers.append([find_int_right_to_left(matrix[i], j-1)])
                numbers.append(find_ints(matrix[i-1], j))
                numbers.append(find_ints(matrix[i+1], j))

                gear_ratios.append( evaluate_and_summerize(numbers))
           
    return gear_ratios


file_path = 'day_3_input_simple.txt'  # Replace with the path to your file
result_char_matrix = create_padded_char_matrix(file_path)

# Print the character matrix
part_numbers = find_part_numbers(result_char_matrix)



file_path = 'day_3_input.txt'  # Replace with the path to your file
result_char_matrix = create_padded_char_matrix(file_path)

# Print the character matrix
# for row in result_char_matrix:
#     print("".join(row))

#part_numbers_2 = find_part_numbers(result_char_matrix)
gear_ratios = find_gear_ratios(result_char_matrix)


#print(f'part 1 test sum is: {sum(part_numbers)}')
#print(f'part 1 sum is: {sum(part_numbers_2)}')
print(f'part 2 sum is: {sum(gear_ratios)}')
