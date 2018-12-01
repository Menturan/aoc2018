from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_list_of_numbers
from puzzle_util.test import test

def part1(input: list) -> int:
    """
Puzzle
    :return sum:
    """
    return sum(input)


def part1_test():
    assert part1([1, 1, 1]) == 3
    assert part1([1, 1, -2]) == 0
    assert part1([-1, -2, -3]) == -6


def part2(input: list) -> int:
    frequenzy = 0
    lista = set([frequenzy])
    frequenzy += input[0]
    index = 1
    while frequenzy not in lista:
        lista.add(frequenzy)
        frequenzy += input[index]
        index += 1
        if index == len(input):
            index = 0
    return frequenzy


def part2_test():
    test(part2([1, -1]), 0)
    test(part2([3, 3, 4, -2, -4]), 10)
    test(part2([-6, 3, 8, 5, -6]), 5)
    test(part2([7, 7, -2, -7, -4]), 14)

print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_numbers('dec_01.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(read_file_to_list_of_numbers('dec_01.txt'))))
