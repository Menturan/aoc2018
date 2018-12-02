from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_list_of_strings
from puzzle_util.test import test

def part1(input: list) -> int:
    no_three_letters = 0
    no_two_letters = 0
    for id in input:
        uniq_letters = set(id)
        has_same_three_letters = False
        has_same_two_letters = False
        for letter in uniq_letters:
            if list(id).count(letter) == 2:
                has_same_two_letters = True
            if list(id).count(letter) == 3:
                has_same_three_letters = True
        if has_same_three_letters:
            no_three_letters += 1
        if has_same_two_letters:
            no_two_letters += 1
    return no_three_letters * no_two_letters


def part1_test():
    testlista = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    test(part1(testlista), 12)


def part2(input: list) -> str:
    for id in input:
        compare_list = input.copy()
        compare_list.remove(id)
        for compare_id in compare_list:
            no_diff_letter_indexes = 0
            latest_idx = 0
            for idx, letter in enumerate(list(id)):
                if list(id)[idx] != list(compare_id)[idx]:
                    no_diff_letter_indexes += 1
                    latest_idx = idx
            if no_diff_letter_indexes == 1:
                result_letters = list(id)
                del result_letters[latest_idx]
                return ''.join(result_letters)

def part2_test():
    test_list = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    test(part2(test_list), 'fgij')


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_strings('dec_02.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(read_file_to_list_of_strings('dec_02.txt'))))
