def get_input_filepath(day):
    """
    Returns relative path to day's input file
    """
    return f'../../docs/inputs/day{day}.txt'

def get_test_input_filepath(day):
    """
    Returns relative path to day's test input file
    """
    return f'../docs/testinputs/day{day}.txt'

def parse_int(string):
    """
    Parses string to int, on error returns None
    """
    try:
        return int(string)
    except ValueError:
        pass

def parse_comma_sep_int_list(filepath):
    """
    Returns list of ints read from provided file
    (see testinputs/comma_sep_int.txt)
    """
    # Read line and close file
    file = open(filepath, "r")
    file_line = file.readline()
    file.close()
    # Separate into values based off comma delim
    numStrs = file_line.split(",")
    nums = [parse_int(i) for i in numStrs]
    return nums

def parse_int_list(filepath):
    """
    Returns list of ints read from provided file
    (see testinputs/int_list.txt)
    """
    # Read line, parsing number read
    file = open(filepath, "r")
    lines = file.readlines()
    nums = [parse_int(i) for i in lines]
    file.close()
    return nums

        

