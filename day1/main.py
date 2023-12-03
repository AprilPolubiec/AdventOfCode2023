import os

num_strings = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def num_string_to_int(num_str: int | str):
    if num_str.isdigit():
        return num_str
    else:
        return num_strings[num_str]


def has_num_string(s: str):
    for num_string in num_strings:
        if s.find(num_string) != -1:
            return num_string
    return False


def get_first_and_last_digit(line: str):
    string_check_start_idx = 0
    nums = []

    for idx, char in enumerate(line):
        if char.isdigit():
            nums.append(int(char))
            continue
        num_string = has_num_string(line[string_check_start_idx:idx + 1])
        if num_string != False:
            nums.append(num_string_to_int(num_string))
            string_check_start_idx = idx
            continue
    return [nums[0], nums[-1]]
    

    

def get_sum(filename: str):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_dir, filename)
    f = open(input_file_path, "r")

    lines = f.readlines()

    sum = 0
    for line in lines:
        ints = get_first_and_last_digit(line)
        if len(ints) > 0:
            sum += int(str(ints[0]) + str(ints[-1]))
    return sum

if __name__ == '__main__':
    res = get_sum("input.txt")
    print(res)
