# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def solve(message: str, distinct_characters_number: int) -> int:
    for i in range(0, len(message)):
        if len(set(message[i:i + distinct_characters_number])) == distinct_characters_number:
            return i + distinct_characters_number
    return 0


def part_one(file) -> int:
    message = file.readline()
    distinct_characters_number = 4
    res = solve(message, distinct_characters_number)
    return res


def part_two(file) -> int:
    message = file.readline()
    distinct_characters_number = 14
    res = solve(message, distinct_characters_number)
    return res


def read_file():
    return open("input.txt", "r")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file()
    # print(part_one(file))
    print(part_two(file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
