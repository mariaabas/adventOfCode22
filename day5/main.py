# This is a sample Python script.
import re


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# stacks = {
# "1": ["Z", "N"],
# "2": ["M", "C", "D"],
# "3": ["P"]
# }

stacks = {
    "1": ["R", "S", "L", "F", "Q"],
    "2": ["N", "Z", "Q", "G", "P", "T"],
    "3": ["S", "M", "Q", "B"],
    "4": ["T", "G", "Z", "J", "H", "C", "B", "Q"],
    "5": ["P", "H", "M", "B", "N", "F", "S"],
    "6": ["P", "C", "Q", "N", "S", "L", "V", "G"],
    "7": ["W", "C", "F"],
    "8": ["Q", "H", "G", "Z", "W", "V", "P", "M"],
    "9": ["G", "Z", "D", "L", "C", "N", "R"]

}


def parse_movements(line):
    return re.findall('[0-9]+', line)


def part_one(file):
    line = file.readline()
    while line:
        movements = parse_movements(line)
        # aux = stacks[movements[1]]
        # stacks[movements[2]] = stacks[movements[2]] + aux[]
        stack = stacks[movements[1]]
        for i in range(0, int(movements[0])):
            stacks[movements[2]] += stack[len(stack) - i - 1]
        stack = stack[0:len(stack) - int(movements[0])]
        stacks[movements[1]] = stack
        line = file.readline()
    result = ""
    for s in stacks.values():
        result += s[-1]
    return result


def part_two(file):
    line = file.readline()
    while line:
        movements = parse_movements(line)
        stack = stacks[movements[1]]
        stacks[movements[2]] += stack[len(stack) - int(movements[0])::]
        stacks[movements[1]] = stack[0:len(stack) - int(movements[0])]
        line = file.readline()
    result = ""
    for s in stacks.values():
        result += s[-1]
    return result


def read_file():
    return open("input.txt", "r")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    file = read_file()
    #print(part_one(file))
    print(part_two(file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
