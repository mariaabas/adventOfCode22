# This is a sample Python script.
from interval import interval


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def parse_intervals(line):
    intervals = line.split(",")
    return intervals[0].split("-") + intervals[1].split("-")


def part_two(file):
    line = file.readline().strip()
    suma = 0
    while line:
        list_intervals = parse_intervals(line)
        result = interval[int(list_intervals[0]), int(list_intervals[1])] & interval[int(list_intervals[2]), int(list_intervals[3])]
        if result:
            suma += 1
        line = file.readline().strip()
    return suma


def part_one(file):
    line = file.readline().strip()
    suma = 0
    while line:
        list_intervals = parse_intervals(line)
        result = (interval[int(list_intervals[0]), int(list_intervals[1])] in interval[
            int(list_intervals[2]), int(list_intervals[3])]) or \
                 (interval[int(list_intervals[2]), int(list_intervals[3])] in interval[
                     int(list_intervals[0]), int(list_intervals[1])])
        suma += result
        line = file.readline().strip()
    return suma


def read_file():
    return open("input.txt", "r")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file()
    # print(part_one(file))
    print(part_two(file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
