from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_string
from puzzle_util.test import test
from timeit import default_timer as timer


def part1(polymer: str) -> int:
    index = 0
    polymer = polymer
    while (True):
        if len(polymer) == index + 1:
            return len(polymer)
        char1 = polymer[index]
        char2 = polymer[index + 1]
        if char1.lower() == char2.lower() and char1 != char2:  # Samma bokstav fast stor och liten (Aa)
            polymer = polymer.replace(polymer[index] + polymer[index + 1], '')
            index = 0
        else:
            if index == len(polymer):
                return len(polymer)
            index += 1


def part1_test():
    test(part1('dabAcCaCBAcCcaDA'), 10)  # dabCBAcaDA


def part2(polymer: str) -> int:
    polymer_count = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'x', 'y', 'z']
    for letter in letters:
        polymer_copy = polymer
        polymer_copy = polymer_copy.replace(letter, '')
        polymer_copy = polymer_copy.replace(letter.upper(), '')
        polymer_count.append(part1(polymer_copy))
    polymer_count.sort()
    return polymer_count[0]



def part2_test():
    test(part2('dabAcCaCBAcCcaDA'), 4)  # dabAaBAaDA


print(tree)
print('### Part 1 ###')
part1_test()
start = timer()
print('Resultat: ' + str(part1(read_file_to_string('dec_05.txt'))))
end = timer()
print('Tid: {0:.3f}s'.format(end - start))
print('### Part 2 ###')
part2_test()
start = timer()
print('Resultat: ' + str(part2(read_file_to_string('dec_05.txt'))))
end = timer()
print('Tid: {0:.3f}s'.format(end - start))
