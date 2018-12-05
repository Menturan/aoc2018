from puzzle_util.christmas_tree import tree
# from puzzle_util.read_file import någon_func
from puzzle_util.test import test
from timeit import default_timer as timer


def part1(input) -> int:
    pass


def part1_test():
    test(0, 0)


def part2(input) -> int:
    pass


def part2_test():
    test(0, 0)


print(tree)
print('### Part 1 ###')
part1_test()
start = timer()
print('Resultat: ' + str(part1('')))
end = timer()
print('Tid: {0:.3f}s'.format(end - start))
print('### Part 2 ###')
part2_test()
start = timer()
print('Resultat: ' + str(part2('')))
end = timer()
print('Tid: {0:.3f}s'.format(end - start))
