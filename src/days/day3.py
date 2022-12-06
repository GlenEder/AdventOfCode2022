import math

from src.utils.io_handlers.input_handler import get_input_filepath, get_string_list
from src.utils.io_handlers.output_handler import print_day_info

def getPriority(abc):
    u_case = ord(abc) - ord('a')
    return ord(abc) - ord('A')  + 27 if u_case < 0 else u_case + 1

def day3(inputfile):
    prioritySum = 0
    groupIndex = 0
    groupItems = ["", "", ""]
    groupPrioritySum = 0
    for line in get_string_list(inputfile):
        middle = math.floor(len(line) / 2)
        front = line[0:middle]
        back = line[middle:len(line)]
        matchFound = False
        for char in front:
            if not matchFound and char in back:
                prioritySum += getPriority(char)
                matchFound = True

        # Part 2
        groupItems[groupIndex] = line
        groupIndex += 1
        if groupIndex > 2:
            # Find match between all three strings
            for char in groupItems[0]:
                if char in groupItems[1] and char in groupItems[2]:
                    groupPrioritySum += getPriority(char)
                    break
            groupIndex = 0


    print_day_info(3, prioritySum, groupPrioritySum)


if __name__ == "__main__":
    day3(get_input_filepath(3))