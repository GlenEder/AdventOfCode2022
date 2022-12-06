from src.utils.io_handlers.input_handler import get_input_filepath, get_string_list
from src.utils.io_handlers.output_handler import print_day_info

THEIR_ROCK = 'A'
THEIR_PAPER = 'B'
THEIR_SCISSORS = 'C'
ROCK = 'X' # Loss
PAPER = 'Y' # Tie
SCISSORS = 'Z' # Win


def win(abc, xyz):
    # This method cals wins based off the diff of the ascii values (left here for knowledge’s sake)
    their_val = ord(abc) - ord('A')
    our_val = ord(xyz) - ord('X')
    diff = their_val - our_val
    if diff == 0:
        return 3
    elif diff == 1 or diff == -2:
        return 0
    elif diff == -1 or diff == 2:
        return 6

def winnings(abc, xyz):
    """
    6 - win, 3 - tie, 0 loss
    """
    if abc == THEIR_ROCK:
        if xyz == ROCK:
            return 3
        elif xyz == PAPER:
            return 6
        else:
            return 0
    elif abc == THEIR_PAPER:
        if xyz == ROCK:
            return 0
        elif xyz == PAPER:
            return 3
        else:
            return 6
    else:
        if xyz == ROCK:
            return 6
        elif xyz == PAPER:
            return 0
        else:
            return 3


def bonus(xyz):
    if xyz == ROCK:
        return 1
    elif xyz == PAPER:
        return 2
    else:
        return 3

def ourScoringMove(abc, outcome):
    LOSS = 'X'
    DRAW = 'Y'
    WIN = 'Z'
    if abc == THEIR_ROCK:
        if outcome == LOSS:
            return bonus(SCISSORS)
        elif outcome == DRAW:
            return bonus(ROCK) + 3
        else:
            return bonus(PAPER) + 6
    elif abc == THEIR_PAPER:
        if outcome == LOSS:
            return bonus(ROCK)
        elif outcome == DRAW:
            return bonus(PAPER) + 3
        else:
            return bonus(SCISSORS) + 6
    else:
        if outcome == LOSS:
            return bonus(PAPER)
        elif outcome == DRAW:
            return bonus(SCISSORS) + 3
        else:
            return bonus(ROCK) + 6

def calc_winnings(abc, xyz):
    return bonus(xyz) + winnings(abc, xyz)


def day2(inputfile):
    rpsRounds = get_string_list(inputfile)
    score = 0
    outcome_score = 0
    for round in rpsRounds:
        if round is not None:
            theirMove = round[0]
            ourMove = round[2]
            score += calc_winnings(theirMove, ourMove)
            outcome_score += ourScoringMove(theirMove, ourMove)

    print_day_info(2, score, outcome_score)




if __name__ == '__main__':
    day2(get_input_filepath(2))