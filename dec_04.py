from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_list_of_strings
from puzzle_util.test import test

def parse_and_sort_calendar(unsorted_calendar: list) -> list:
    sorted_calendar = {}
    for calendar_post in unsorted_calendar:
        date = calendar_post[1:11] # 1518-11-01
        time = calendar_post[1:11]
        note = calendar_post[19:]
        if date not in sorted_calendar:
            sorted_calendar[date] = {}
        if time not in sorted_calendar[date]:
            sorted_calendar[date][time] = ''
        sorted_calendar[date][time] = note
        

def part1(schedule: list) -> int:
    pass


def part1_test():
    test_input = read_file_to_list_of_strings('dec_04_test_input.txt')
    test(part1(test_input), 240)


def part2(input) -> int:
    pass


def part2_test():
    test(0,0)


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_strings('dec_04.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2([])))
