from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_list_of_strings
from puzzle_util.test import test


def convert_to_dict_and_calculate(claim: str) -> dict:
    # #1 @ 1,3: 4x4
    splitted = claim.split(' ')  # [#1, @, 1,3:, 4x4]
    xy = splitted[2].replace(':', '').split(',')  # [1, 3]
    size = splitted[3].split('x')  # [4, 4]
    return {'x': int(xy[0]), 'y': int(xy[1]), 'wide': int(size[0]), 'tall': int(size[1]),
            'x_end': int(xy[0]) + int(size[0]), 'y_end': int(xy[1]) + int(size[1])}


def part1(claims: list) -> int:
    inches_overlapping = 0
    for claim in set(claims):
        compare_claims = set(claims.copy())
        compare_claims.remove(claim)
        claim = convert_to_dict_and_calculate(claim)
        print('Claim: %s' % claim)
        for compare_claim in compare_claims:
            compare_claim = convert_to_dict_and_calculate(compare_claim)
            print('Compare claim: %s' % compare_claim)
            if (claim['x'] < compare_claim['x_end'] and claim['x_end'] > compare_claim['x'] and
                    claim['y'] > compare_claim['y_end'] and claim['y_end'] < compare_claim['y']):
                x = max(claim['x'], compare_claim['x'])
                y = max(claim['y'], compare_claim['y'])
                tall = min(claim['y_end'], compare_claim['y_end']) - y
                wide = min(claim['x_end'], compare_claim['x_end']) - x
                inches_overlapping += wide * tall
    return inches_overlapping


def part1_test():
    test_input = ['#1 @ 1,3: 4x4',
                  '#2 @ 3,1: 4x4',
                  '#3 @ 5,5: 2x2']
    """
    ........
    ...2222.
    ...2222.
    .11XX22.
    .11XX22.
    .111133.
    .111133.
    ........
    """
    test(part1(test_input), 4)


def part2(input) -> int:
    pass


def part2_test():
    test(0, 0)


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_strings('dec_03.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(read_file_to_list_of_strings('dec_03.txt'))))
