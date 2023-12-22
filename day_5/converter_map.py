
    from range_converter import RangeConverter
from range import Range

class ConverterMap:
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination
        self.range_converters = []

    def add_range_converter(self, range_converter: RangeConverter):
        self.range_converters.append(range_converter)

    def _get_lines(self) -> [str]:
        lines = []
        lines.append(f'{self.source}-to-{self.destination} map:\n')
        for range_converter in self.range_converters:
            lines.append(range_converter.print())
        return lines
    
    def print(self):
        lines = self._get_lines()
        for line in lines:
            print(line)
    
    def print_to_file(self, filepath):
        file = open(filepath, 'a')
        lines = self._get_lines()
        for line in lines:
                file.write(line)
        
        file.write('\n')

    def convert_single_value(self, input: int) -> int:
        print(f'input:{input}')

        for range_converter in self.range_converters:
            if range_converter.is_inside_range_single_value(input):
                return range_converter.convert_single_value(input)
        
        return input
    
    def convert_range_vector(self, input_ranges: [Range]) -> [Range]:
        output_ranges = []        

        for input_range in input_ranges:
            was_found = False
            for range_converter in self.range_converters:
                if range_converter.is_inside_range_range(input_range):
                    output_ranges.extend(range_converter.convert_range(input_range))
                    was_found = True

            if not was_found:
                output_ranges.extend([input_range])

        return output_ranges