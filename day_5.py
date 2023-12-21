
import re

from time import sleep
from tqdm import tqdm

class Range:
    def __init__(self, start, length):
        self.start = start
        self.length = length

class MasterConverter:
    def __init__(self, range_converters):
        self.range_converters = range_converters

    def convert_single_value(self, source, destination, input):
        print(f'source:{source} - destination:{destination} : input:{input}')
    
        for range_converter in self.range_converters:
            if range_converter.source == source:
                temp_output = range_converter.convert_single_value(input)
                
                if range_converter.destination == destination:
                    return temp_output
                else:
                    return [self.convert_single_value(range_converter.destination, destination, temp_output)]
    
        print(f'source:{source} - destination:{destination} : input:{input}. MUST NOT COME HERE')
        return None

    def convert_range(self, source, destination, range):
        
        for range_converter in self.range_converters:
            if range_converter.source == source:
                temp_range_vector = range_converter.convert_range_vector([range])
                
                if range_converter.destination == destination:
                    return temp_range_vector
                else:
                    return self.convert_range_vector(range_converter.destination, destination, temp_range_vector)
    
        print(f'source:{source} - destination:{destination} : range:{input}. MUST NOT COME HERE')
        return None
    

    def convert_range_vector(self, source, destination, range_vector):
        out = []
        
        for range in range_vector:
            #out += self.convert(source, destination, range)
            out += self.convert_range(source, destination, range)

        return out

class RangeConverter:
    def __init__(self, source_start, destination_start, range_length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.range_length = range_length

    def is_inside_range_single_value(self, input):
        if input < self.source_start:
            return False
        if input > self.source_start + self.range_length:
            return False
       
        return True
    
    def is_inside_range_range(self, input_range):
        if input_range.start + input_range.length < self.source_start:
            return False
        if input_range.start > self.source_start + self.range_length:
            return False
       
        return True
    
    def convert_single_value(self, input):
        if self.is_inside_range_single_value(input):
            diff = input - self.source_start
            return self.destination_start + diff
        
        return input

    def convert_range(self, input_range):
        print(f'input_range. start:{input_range.start}. length:{input_range.length}')

        input_starts_before_convertion = input_range.start < self.source_start
        input_ends_after_convertion = input_range.start + input_range.length > self.source_start + self.range_length

        case_id = 0

        if input_starts_before_convertion and input_ends_after_convertion:
            case_id = 1
        elif input_starts_before_convertion and not input_ends_after_convertion:
            case_id = 2
        elif not input_starts_before_convertion and not input_ends_after_convertion:
            case_id = 3
        else:
            case_id = 4

        print(f'start_before:{input_starts_before_convertion} and ends_after:{input_ends_after_convertion} case_id:{case_id}')


        output_ranges = []
        input_range_consumed = 0

        # Input range before convertor. just create range
        if case_id == 1 or case_id == 2:
            start_diff = self.source_start - input_range.start
            first_range = start_diff
            input_range_consumed += first_range
            output_ranges.append(Range(input_range.start, first_range))
        
        # Input range inside convertor. all must be converted
        if case_id == 1:
            new_start = self.convert_single_value(self.source_start)
            new_range = self.range_length
            output_ranges.append(Range(new_start, new_range))
            print(f'case_id:{case_id}, new_start:{new_start} new_range:{new_range}')
            input_range_consumed += new_range

        elif case_id == 2:
            new_start = self.convert_single_value(self.source_start)
            new_range = input_range.length - input_range_consumed

            print(f'case_id:{case_id}, new_start:{new_start} new_range:{new_range}')
            output_ranges.append(Range(new_start, new_range))
            input_range_consumed += new_range
            #return output_ranges
        
        elif case_id == 3:
            new_start = self.convert_single_value(input_range.start)
            new_range = self.range_length - input_range.start

            print(f'case_id:{case_id}, new_start:{new_start} new_range:{new_range}')
            output_ranges.append(Range(new_start, new_range))
            input_range_consumed += new_range

        elif case_id == 4:
            new_start = self.convert_single_value(input_range.start)
            new_range = self.range_length

            print(f'case_id:{case_id}, new_start:{new_start} new_range:{new_range}')
            output_ranges.append(Range(new_start, new_range))
            input_range_consumed += new_range
            #return output_ranges


        # Input range after convertor. just create range
        if case_id == 1 or case_id == 3:
            new_start = self.source_start + self.range_length
            new_range = input_range.length - input_range_consumed

            print(f'case_id:{case_id}, new_start:{new_start} new_range:{new_range}')
            output_ranges.append(Range(new_start, new_range))
            input_range_consumed += new_range
    
        return output_ranges
  
  
class ConverterObject:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.range_converters = []

    def add_range_converter(self, range_converter):
        self.range_converters.append(range_converter)

    def convert_single_value(self, input):
        print(f'input:{input}')

        for range_converter in self.range_converters:
            if range_converter.is_inside_range_single_value(input):
                return range_converter.convert_single_value(input)
        
        return input
    
    def convert_range_vector(self, input_ranges):
        output_ranges = []        

        for input_range in input_ranges:
            for range_converter in self.range_converters:
                if range_converter.is_inside_range_range(input_range):
                    output_ranges += range_converter.convert_range(input_range)
        
        return output_ranges
            

def parse_seeds_range_input(line):
    split_result = line.split(':')
    seed_ranges = split_result[1].split(' ')
    seed_ranges = [int(x) for x in seed_ranges if x]

    list_of_seed_ranges = []
    for i in range(0, len(seed_ranges), 2):
        list_of_seed_ranges.append(Range(seed_ranges[i], seed_ranges[i+1]))
        #list_of_seed_ranges.append([seed_ranges[i], seed_ranges[i+1]])
        
    return list_of_seed_ranges




list_of_seeds = []
list_of_seed_ranges = []
list_of_converters = []

file = open("day_5_input_simple.txt", "r")
is_parsing_converter = False



for line in file:
    if line == "" or line == '\n':
        is_parsing_converter = False
        continue

    elif "seeds:" in line:
        # for part one
        split_result = line.split(':')
        list_of_seeds = split_result[1].split(' ')
        list_of_seeds = [int(x) for x in list_of_seeds if x]
        # for part 2
        list_of_seed_ranges = parse_seeds_range_input(line)

    elif "-to-" in line and " map:" in line:
        split_result = line.split("-to-")
        source = split_result[0]
        destination = split_result[1].split(" ")[0]

        list_of_converters.append(ConverterObject(source, destination))

        is_parsing_converter = True


    elif is_parsing_converter:
        split_result = line.split(' ')
        list_of_ints = [int(x) for x in split_result if x]

        source_start = list_of_ints[1]
        destination_start = list_of_ints[0]
        range_length = list_of_ints[2]

        list_of_converters[-1].add_range_converter(RangeConverter(source_start, destination_start, range_length))
       
master_converter = MasterConverter(list_of_converters)

number_of_seeds = 0
for seed_range in list_of_seed_ranges:
    number_of_seeds += seed_range.length

print(f'NumberOfSeeds:{number_of_seeds}')

# list_of_locations = []
# for i in tqdm(range(len(list_of_seeds))):
#     location = converter.convert("seed", "location", list_of_seeds[i])
#     list_of_locations.append(location)


# print(f"locations are {list_of_locations}")
# print(f"lowest is locations are {min(list_of_locations)}")


#part 2
list_of_locations_ranges = master_converter.convert_range_vector("seed", "location", list_of_seed_ranges)

smallest = 999999999999999999
smallest_not_zero = 999999999999999999
for location_range in list_of_locations_ranges:
    print(f'location start:{location_range.start} \t length:{location_range.length}')

    if location_range.start <= smallest:
        smallest = location_range.start
    if location_range.start <= smallest_not_zero and location_range.start > 0:
        smallest_not_zero = location_range.start

print(f"there are {len(list_of_locations_ranges)} location ranges")
print(f"lowest is locations is: {smallest}")
print(f"lowest (non zero) is locations is: {smallest_not_zero}")