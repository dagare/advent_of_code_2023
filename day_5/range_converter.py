from range import Range

class RangeConverter:
    def __init__(self, source_start: int, destination_start: int, range_length: int):
        self.source_start = source_start
        self.destination_start = destination_start
        self.range_length = range_length

    def print(self):
        return f'{self.destination_start} {self.source_start} {self.range_length}\n'

    def is_inside_range_single_value(self, input: int) -> bool:
        if input < self.source_start:
            return False
        if input > self.source_start + self.range_length:
            return False
       
        return True
    
    def is_inside_range_range(self, input_range: Range) -> bool:
        if input_range.start + input_range.length < self.source_start:
            return False
        if input_range.start > self.source_start + self.range_length:
            return False
       
        return True
    
    def convert_single_value(self, input: int) -> int:
        if self.is_inside_range_single_value(input):
            diff = input - self.source_start
            return self.destination_start + diff
        
        return input

    def convert_range(self, input_range: Range) -> [Range]:
        print(f'input_range. start:{input_range.start}. length:{input_range.length}. self.source_start:{self.source_start} destination_start:{self.destination_start} self.range_lenght:{self.range_length}')

        input_starts_before_convertion = input_range.start < self.source_start
        input_ends_after_convertion = input_range.start + input_range.length > self.source_start + self.range_length

        case_id = 0

        if input_starts_before_convertion and input_ends_after_convertion:
            case_id = 1
        elif input_starts_before_convertion and not input_ends_after_convertion:
            case_id = 2
        elif not input_starts_before_convertion and input_ends_after_convertion:
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
            new_range = self.range_length - (new_start - self.source_start)

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
  


def f -> bool:
        return range_converter_to.is_inside_range_range(Range(range_converter_to.destination_start, range_converter_to.range_length))
