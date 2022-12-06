# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def part_one(file):
    calories = file.readline()
    max_calories = 0
    elf_calories = 0
    while calories:
        if calories == '\n':
            max_calories = elf_calories if elf_calories > max_calories else max_calories
            elf_calories = 0
        else:
            elf_calories = elf_calories + int(calories)

        calories = file.readline()
    return max_calories


def part_two(file):
    calories = file.readline()
    elf_calories = 0
    elfs_calories_list = []
    while calories:
        if calories == '\n':
            elfs_calories_list.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories = elf_calories + int(calories)

        calories = file.readline()

    elfs_calories_list.sort(reverse=True)
    total_elfs_three = elfs_calories_list[0] + elfs_calories_list[1] + elfs_calories_list[2]
    return total_elfs_three


def read_file():
    return open("input.txt", "r")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file()
    #print(part_one(file))
    print(part_two(file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
