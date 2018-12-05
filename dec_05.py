from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_string
from puzzle_util.test import test


def part1(polymer: str) -> int:
    index = 0
    polymer = list(polymer)
    while(True):
        if len(polymer) == index + 1:
            return len(polymer)
        char1 = polymer[index]
        char2 = polymer[index + 1]
        if char1.lower() == char2.lower() and char1 != char2: # Samma bokstav fast stor och liten (Aa)
            polymer.pop(index + 1)
            polymer.pop(index)
            index = 0
        else:
            if index == len(polymer):
                return len(polymer)
            index += 1







def part1_test():
    test(part1('dabAcCaCBAcCcaDA'), 10)  # dabCBAcaDA


def part2(input) -> int:
    pass


def part2_test():
    test(0, 0)


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_string('dec_05.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(read_file_to_string('dec_05.txt'))))
