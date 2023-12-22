
from range import Range
from converter_map import ConverterMap
from range_converter import RangeConverter

class MasterConverter:
    def __init__(self, converter_maps):
        self.converter_maps = converter_maps
        print(f'MasterConverter with {len(self.converter_maps)} converter maps')

    def print_all_to_file(self, filepath: str) -> None:
        print(f'MasterConverter printing to file: {filepath}')

        file = open(filepath, 'w')
        file.close()

        for converter_map in self.converter_maps:
            converter_map.print_to_file(filepath)

        print("MasterConverter done printing to file")

    def print_some_to_file(self, filepath: str, source: str, destination: str) -> None:
        print(f'MasterConverter printing {source}-to-{destination} to file: {filepath}')

        file = open(filepath, 'w')
        file.close()

        converter_map = self.merge_converter_maps(source, destination)

        converter_map.print_to_file(filepath)


    def merge_converter_maps(self, source: str, destination: str) -> ConverterMap:
        for converter_map in self.converter_maps:
            if converter_map.source == source:
                temp_output = converter_map.convert_single_value(converter_map.range_converters)
                
                if converter_map.destination == destination:
                    return temp_output
                else:
                    return [self.convert_single_value(converter_map.destination, destination, temp_output)]
    
        print(f'source:{source} - destination:{destination} : input:{input}. MUST NOT COME HERE')
        return None


    def convert_single_value(self, source: str, destination: str, input: int) -> int:
        print(f'source:{source} - destination:{destination} : input:{input}')
    
        for converter_map in self.converter_maps:
            if converter_map.source == source:
                temp_output = converter_map.convert_single_value(input)
                
                if converter_map.destination == destination:
                    return temp_output
                else:
                    return [self.convert_single_value(converter_map.destination, destination, temp_output)]
    
        print(f'source:{source} - destination:{destination} : input:{input}. MUST NOT COME HERE')
        return None

    def convert_range(self, source: str, destination: str, range: Range) -> [Range]:
        
        for converter_map in self.converter_maps:
            if converter_map.source == source:
                temp_range_vector = converter_map.convert_range_vector([range])
                
                if converter_map.destination == destination:
                    return temp_range_vector
                else:
                    return self.convert_range_vector(converter_map.destination, destination, temp_range_vector)
    
        print(f'source:{source} - destination:{destination} : range:{input}.')
        raise Exception(f'convert_range FAILED. source:{source} - destination:{destination} : range:{input}.')
    

    def convert_range_vector(self, source: str, destination: str, range_vector: [Range]) -> [Range]:
        out = []
        
        for range in range_vector:
            out.extend(self.convert_range(source, destination, range))

        return out
    
    def convert_range_converter(self, source: str, destination: str, range_converter: RangeConverter) -> [RangeConverter]:
        for converter_map in self.converter_maps:
            if converter_map.source == source:
                temp_range_vector = converter_map.convert_range_vector([range])
                
                if converter_map.destination == destination:
                    return temp_range_vector
                else:
                    return self.convert_range_vector(converter_map.destination, destination, temp_range_vector)
    
        print(f'source:{source} - destination:{destination} : range:{input}.')
        raise Exception(f'convert_range_converter FAILED. source:{source} - destination:{destination} : range:{input}.')

    def convert_range_converter_vector(self, source: str, destination: str, range_converter_vector: [RangeConverter]) -> [RangeConverter]:
        out = []
        
        for range_converter in range_converter_vector:
            out.extend(self.convert_range(source, destination, range_converter))

        return out