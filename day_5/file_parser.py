
from converter_map import ConverterMap
from range_converter import RangeConverter
from range import Range


class Config:
    def __init__(self, list_of_seeds, list_of_seed_ranges, list_of_converter_maps):
        self.list_of_seeds = list_of_seeds
        self.list_of_seed_ranges = list_of_seed_ranges
        self.list_of_converter_maps = list_of_converter_maps
        
    def get_list_of_seeds(self) -> [int]:
        return self.list_of_seeds
    
    def get_list_of_seed_ranges(self) -> [Range]:
        return self.list_of_seed_ranges
    
    def get_list_of_converter_maps(self) -> [ConverterMap]:
        return self.list_of_converter_maps

def _parse_seeds_range_input(line):
    split_result = line.split(':')
    seed_ranges = split_result[1].split(' ')
    seed_ranges = [int(x) for x in seed_ranges if x]

    list_of_seed_ranges = []
    for i in range(0, len(seed_ranges), 2):
        list_of_seed_ranges.append(Range(seed_ranges[i], seed_ranges[i+1]))
        #list_of_seed_ranges.append([seed_ranges[i], seed_ranges[i+1]])
        
    return list_of_seed_ranges


def parse_file(file_path) -> Config:
    print(f"parse_file:{file_path}")

    file = open(file_path, "r")
    is_parsing_converter = False

    list_of_seeds = []
    list_of_seed_ranges = []
    list_of_converter_maps = []

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
            list_of_seed_ranges = _parse_seeds_range_input(line)

        elif "-to-" in line and " map:" in line:
            split_result = line.split("-to-")
            source = split_result[0]
            destination = split_result[1].split(" ")[0]

            list_of_converter_maps.append(ConverterMap(source, destination))

            is_parsing_converter = True


        elif is_parsing_converter:
            split_result = line.split(' ')
            list_of_ints = [int(x) for x in split_result if x]

            source_start = list_of_ints[1]
            destination_start = list_of_ints[0]
            range_length = list_of_ints[2]

            list_of_converter_maps[-1].add_range_converter(RangeConverter(source_start, destination_start, range_length))

    return Config(list_of_seeds, list_of_seed_ranges, list_of_converter_maps)
    





