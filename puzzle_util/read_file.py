def read_file_to_string(filename, with_lines=False) -> str:
    with open('puzzle_input/' + filename) as f:
        text = f.read()
        if not with_lines:
            text = text.replace('\n', '')
        return text


def read_file_to_list_of_strings(filename) -> list:
    with open('puzzle_input/' + filename) as f:
        return f.read().splitlines()


def read_file_to_list_of_numbers(filename) -> list:
    with open('puzzle_input/' + filename) as f:
    #with open(os.path.abspath(os.path.join('puzzle_input/' + filename, os.pardir)) + '/' +filename) as f:
        list_of_strings = f.read().splitlines()
        for idx, string in enumerate(list_of_strings):
            list_of_strings[idx] = int(string)
        return list_of_strings
