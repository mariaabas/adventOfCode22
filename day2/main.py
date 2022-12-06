# This is a sample Python script.
from enum import Enum


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class RockPaperScissorsOpponent(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class RockPaperScissorsMe(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


hashmap_value = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

WIN_POINTS = 6
DRAW_POINTS = 3


def part_one(file):
    game_round = file.readline()
    total_result = 0
    while game_round:
        opponent_result = game_round[0]
        me_result = game_round[2]

        if opponent_result == RockPaperScissorsOpponent.ROCK.value:
            if me_result == RockPaperScissorsMe.PAPER.value:
                total_result = total_result + WIN_POINTS + hashmap_value[me_result]
            elif me_result == RockPaperScissorsMe.ROCK.value:
                total_result = total_result + DRAW_POINTS + hashmap_value[me_result]
            else:
                total_result = total_result + hashmap_value[me_result]

        elif opponent_result == RockPaperScissorsOpponent.PAPER.value:
            if me_result == RockPaperScissorsMe.SCISSORS.value:
                total_result = total_result + WIN_POINTS + hashmap_value[me_result]
            elif me_result == RockPaperScissorsMe.PAPER.value:
                total_result = total_result + DRAW_POINTS + hashmap_value[me_result]
            else:
                total_result = total_result + hashmap_value[me_result]

        elif opponent_result == RockPaperScissorsOpponent.SCISSORS.value:
            if me_result == RockPaperScissorsMe.ROCK.value:
                total_result = total_result + WIN_POINTS + hashmap_value[me_result]
            elif me_result == RockPaperScissorsMe.SCISSORS.value:
                total_result = total_result + DRAW_POINTS + hashmap_value[me_result]
            else:
                total_result = total_result + hashmap_value[me_result]

        game_round = file.readline()
    return total_result


def read_file():
    return open("input.txt", "r")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file()
    print(part_one(file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
