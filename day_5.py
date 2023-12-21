
import re

from time import sleep
from tqdm import tqdm

class Range:
    def __init__(self, start, range):
        self.start = start
        self.range = range

class Converter:
    def __init__(self, converters):
        self.converters = converters

  

    def convert(self, source, destination, input):
        print(f'source:{source} - destination:{destination} : input:{input}')
    
        for converter in self.converters:
            if converter.source == source:
                temp_output = converter.convert_source_to_destination(input)
                
                if converter.destination == destination:
                    return temp_output
                else:
                    return self.convert(converter.destination, destination, temp_output)
    
        print(f'source:{source} - destination:{destination} : input:{input}. MUST NOT COME HERE')
        return None

    def convert(self, source, destination, range):
        out = []
        
        for range in range_vector:
            out.append(self.convert(source, destination, range))
            
        return out
    

    def convert(self, source, destination, range_vector):
        out = []
        
        for range in range_vector:
            out.append(self.convert(source, destination, range))

        return out

class ConverterRange:
    def __init__(self, source_start, destination_start, range_length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.range_length = range_length

    def is_inside_range(self, input):
        if input < self.source_start:
            return False
        if input > self.source_start + self.range_length:
            return False
       
        return True
    
    def is_inside_range(self, input_range):
        if input_range.start + input_range.range < self.source_start:
            return False
        if input_range.start > self.source_start + self.range_length:
            return False
       
        return True
    
    def convert_single_value(self, input):
        if self.is_inside_range(input):
            diff = input - self.source_start
            return self.destination_start + diff
        
        return input

    def convert_source_to_destination(self, input_range):
        print(f'input:{input}')

        input_starts_before_convertion = input_range.start < self.source_start
        input_ends_after_convertion = input_range.start + input_range.range > self.source_start + self.range_length

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
            new_range = input_range.range - input_range_consumed

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
            new_range = input_range.range - input_range_consumed

            print(f'case_id:{case_id}, new_start:{new_start} new_range:{new_range}')
            output_ranges.append(Range(new_start, new_range))
            input_range_consumed += new_range


        # if (input_range.start <= self.source_start):
        #     # First part with no convertion
        #     start_diff = self.source_start - input_range.start
        #     first_range = min(input_range.range, self.range_length - start_diff)

        #     output_ranges.append(Range(input_range.start, first_range))

        #     if input_range.start + input_range.range <= self.source_start + self.range_length:
        #         return output_ranges
            
        #     # Second is converted
        #     second_range = min(input_range.range, self.range_length)

        #     output_ranges.append(Range(input_range.start, second_range))

        #     if input_range.range > self.range_length:
        #         # We must add the last range
        #         third_start = input_range.start + first_range + second_range
        #         output_ranges.append(Range(third_start, input_range.range-second_range-first_range))

        # else: #(input_range.start > self.source_start):


    
        #return self.destination_start + (input - self.source_start)
    
        return output_ranges
  
  
class ConverterObject:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.converter_ranges = []

    def add_range(self, range):
        self.converter_ranges.append(range)

    def convert_source_to_destination(self, input):
        print(f'input:{input}')

        for range in self.converter_ranges:
            if range.is_inside_range(input):
                return range.convert_source_to_destination(input)
        
        return input
    
    def convert_source_to_destination(self, input_ranges):
        output_ranges = []        

        for input_range in input_ranges:
            for range in self.converter_ranges:
                if range.is_inside_range(input):
                    return range.convert_source_to_destination(input)
        
        return input
            

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

file = open("day_5_input.txt", "r")
is_parsing_converter = False

parse_seeds_as_ranges = True


for line in file:
    if line == "" or line == '\n':
        is_parsing_converter = False
        continue

    elif "seeds:" in line:
        if not parse_seeds_as_ranges:
            split_result = line.split(':')
            list_of_seeds = split_result[1].split(' ')
            list_of_seeds = [int(x) for x in list_of_seeds if x]
        else:
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

        list_of_converters[-1].add_range(ConverterRange(source_start, destination_start, range_length))
       
converter = Converter(list_of_converters)

number_of_seeds = 0
for seed_range in list_of_seed_ranges:
    number_of_seeds += seed_range.range

print(f'NumberOfSeeds:{number_of_seeds}')

list_of_locations = []
for i in tqdm(range(len(list_of_seeds))):
    location = converter.convert("seed", "location", list_of_seeds[i])
    list_of_locations.append(location)


print(f"locations are {list_of_locations}")
print(f"lowest is locations are {min(list_of_locations)}")


#part 2
