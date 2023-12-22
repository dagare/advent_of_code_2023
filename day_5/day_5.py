
from time import sleep
from tqdm import tqdm


from master_converter import MasterConverter
from file_parser import Config, parse_file

a = []
a.append([1,2])
a.append([3,4])

b = []
b += [1, 2]
b += [3, 4]

c = []
c.append(1)
c.append(2)
c.append(3)
c.append(4)

d = []
d.extend([1, 2])
d.extend([3, 4])

e = []
e.extend([[1, 2]])
e.extend([3])
e.extend([4])


#config = parse_file("/home/dat/code/advent_of_code_2023/day_5/day_5_input_simple.txt")
config = parse_file("day_5/day_5_input_simple.txt")

print(f'Number of converter maps:{len(config.get_list_of_converter_maps())}')
master_converter = MasterConverter(config.get_list_of_converter_maps())

# number_of_seeds = 0
# for seed_range in config.get_list_of_seed_ranges():
#     number_of_seeds += seed_range.length

# print(f'NumberOfSeeds:{number_of_seeds}')

# list_of_locations = []
# for i in tqdm(range(len(list_of_seeds))):
#     location = converter.convert("seed", "location", list_of_seeds[i])
#     list_of_locations.append(location)


# print(f"locations are {list_of_locations}")
# print(f"lowest is locations are {min(list_of_locations)}")


master_converter.print_to_file("/home/dat/code/advent_of_code_2023/day_5/debug.txt", "seed", "fertilizer")
#master_converter.print_to_file("day_5/debug_file.txt", "seed", "fertilizer")

#part 2
list_of_locations_ranges = master_converter.convert_range_vector("seed", "soil", config.get_list_of_seed_ranges())

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