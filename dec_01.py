from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_list_of_numbers


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


def part2(input) -> int:
    """
Puzzle
    :return sum:
    """
    pass


def part2_test():
    pass


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_numbers('dec_01.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2("")))
