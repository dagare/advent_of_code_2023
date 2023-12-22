
from converter_map import ConverterMap
from range_converter import RangeConverter, is_inside_range_range_converter

def merge_two_converter_maps(converter_map_from: ConverterMap, converter_map_to: ConverterMap) -> ConverterMap:
    if not converter_map_from.destination == converter_map_to.source:
        print(f'ERROR!!!')

    merged_converter_map = ConverterMap(converter_map_from.source, converter_map_to.destination)

    for range_converter_from in converter_map_from.range_converters:
        is_affected_in_any = False
        
        for range_converter_to in converter_map_to.range_converters:
            if is_inside_range_range_converter(range_converter_from, range_converter_to):

                

        if not is_affected_in_any:
            # Just add it
            merge_converter_maps.add_range_converter(range_converter_from)

    return merged_converter_map

def merge_converter_maps(converter_maps: [ConverterMap], source: str, destination: str) -> ConverterMap:

    merged_converter_map = ConverterMap(source, destination)

    # TODO

    return merged_converter_map
