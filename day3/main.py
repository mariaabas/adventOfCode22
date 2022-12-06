# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def read_file():
    return open("input.txt", "r")


def convert_to_priority(element):
    if element.islower():
        return ord(element) - ord("a") + 1
    else:
        return ord(element) - ord("A") + 27


def part_one(file):
    rucksack = file.readline()
    suma = 0
    while rucksack:
        first_compartment = list(rucksack[0:int(len(rucksack) / 2)])
        second_compartment = list(rucksack[int(len(rucksack) / 2)::])
        result = [value for value in first_compartment if value in second_compartment][0]
        suma += convert_to_priority(element=result)
        rucksack = file.readline()
    return suma


def part_two(file):
    first_compartment = file.readline()
    second_compartment = file.readline()
    third_compartment = file.readline()
    suma = 0
    while first_compartment and second_compartment and third_compartment:
        aux_intersection = [value for value in first_compartment if value in second_compartment]
        result = [value for value in aux_intersection if value in third_compartment][0]
        suma += convert_to_priority(element=result)
        first_compartment = file.readline()
        second_compartment = file.readline()
        third_compartment = file.readline()
    return suma


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file()
    # print(part_one(file))
    print(part_two(file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
