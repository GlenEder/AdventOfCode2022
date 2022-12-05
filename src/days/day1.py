from utils.io_handlers.input_handler import parse_int_list, get_input_filepath
from utils.io_handlers.output_handler import print_day_info
from utils.number_handlers.max_number_list import MaxNumberList

def day1(input_filepath):
    # read input
    elfCalories = parse_int_list(input_filepath)
    maxCalories = MaxNumberList(3)
    currElfCalories = 0
    for num in elfCalories:
        if num is not None:
            currElfCalories += num
        else:
            maxCalories.add(currElfCalories)
            currElfCalories = 0
    # Add last elf's calories
    maxCalories.add(currElfCalories)


    print_day_info(1, maxCalories.max(), maxCalories.sum())


if __name__ == '__main__':
    day1(get_input_filepath(1))