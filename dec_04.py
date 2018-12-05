from puzzle_util.christmas_tree import tree
from puzzle_util.read_file import read_file_to_list_of_strings
from puzzle_util.test import test

def parse_list_of_guards_asleep_time(calendar: list) -> dict:
    guards = {}
    guard_id = 0
    minute_latest_guard_falls_asleep = 0
    for time_slot in sorted(calendar):
        # Time slot = '[1518-11-01 00:00] Guard #10 begins shift'
        note = time_slot[19:]
        if note.startswith('Guard'):
            guard_id = int(note.split(' ')[1].replace('#', '')) 
            if guard_id not in guards:
                guards[guard_id] = [0 for i in range(60)]
        if note == 'falls asleep':
            minute = int(time_slot[15:17])
            minute_latest_guard_falls_asleep = minute
        if note == 'wakes up':
            minute_wakes_up = int(time_slot[15:17])
            for minute in range(minute_latest_guard_falls_asleep, minute_wakes_up):
                guards[guard_id][minute] += 1
    return guards

def part1(schedule: list) -> int:
    guards_asleep = parse_list_of_guards_asleep_time(schedule)
    guards_asleep_sum = guards_asleep.copy()
    for guard in guards_asleep:
        minutes_asleep = sum(guards_asleep[guard])
        guards_asleep_sum[guard] = minutes_asleep
    guard_most_asleep = sorted(guards_asleep_sum, key=guards_asleep_sum.get, reverse=True)[0]
    minute_most_asleep = sorted(guards_asleep[guard_most_asleep], reverse=True)[0]
    guard_most_asleep_minute = guards_asleep[guard_most_asleep].index(minute_most_asleep)
    return guard_most_asleep * guard_most_asleep_minute

def part1_test():
    test_input = read_file_to_list_of_strings('dec_04_test_input.txt')
    test(part1(test_input), 240)


def part2(schedule: list) -> int:
    guards_asleep = parse_list_of_guards_asleep_time(schedule)
    guards_asleep_most_minute = guards_asleep.copy()
    for guard in guards_asleep:
        no_times_sleep_at_specific_minute = sorted(guards_asleep[guard], reverse=True)[0]
        guards_asleep_most_minute[guard] = no_times_sleep_at_specific_minute
    guard_most_asleep = sorted(guards_asleep_most_minute, key=guards_asleep_most_minute.get, reverse=True)[0]
    minute_most_asleep = sorted(guards_asleep[guard_most_asleep], reverse=True)[0]
    guard_most_asleep_minute = guards_asleep[guard_most_asleep].index(minute_most_asleep)
    return guard_most_asleep * guard_most_asleep_minute


def part2_test():
    test_input = read_file_to_list_of_strings('dec_04_test_input.txt')
    test(part2(test_input), 4455)


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_strings('dec_04.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(read_file_to_list_of_strings('dec_04.txt'))))
