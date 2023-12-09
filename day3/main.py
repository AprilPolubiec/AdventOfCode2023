
import os

def read_file(filename: str):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r") as f:
        lines = f.readlines()
    return lines

def is_symbol(c: str):
    return c is not None and not c.isdigit() and not c == "."
def is_asterisk(c: str):
    return c == "*"

def get_neighbors(all_neighbors: [[]], current_pos: ()):
    row_idx = current_pos[0]
    col_idx = current_pos[1]
    num_columns = len(all_neighbors[0])
    num_rows = len(all_neighbors)
    
    left =  all_neighbors[row_idx][col_idx - 1] if col_idx > 0 else None
    right = all_neighbors[row_idx][col_idx + 1] if col_idx < num_columns - 1 else None

    top = all_neighbors[row_idx - 1][col_idx] if row_idx > 0 else None
    bottom = all_neighbors[row_idx + 1][col_idx] if row_idx < num_rows - 1 else None

    top_left = all_neighbors[row_idx - 1][col_idx - 1] if row_idx > 0 and col_idx > 0 else None
    top_right = all_neighbors[row_idx - 1][col_idx + 1] if row_idx > 0 and col_idx < num_columns - 1 else None
    bottom_left = all_neighbors[row_idx + 1][col_idx - 1] if row_idx < num_rows - 1 and col_idx > 0 else None
    bottom_right = all_neighbors[row_idx + 1][col_idx + 1] if row_idx < num_rows - 1 and col_idx < num_columns - 1 else None

    return (left, right, top, bottom, top_left, top_right, bottom_left, bottom_right)

# Given a string, returns as an array where each digit is stored in full in each index it occupies
def create_matrix(in_str: list[str]):
    char_matrix = [ [c for c in l] for l in in_str ]

    current_num_start = None
    current_num = ""

    for row_idx in range(len(char_matrix)):
        row = char_matrix[row_idx]
        for char_idx in range(len(row)):
            char = row[char_idx]
            if not char.isdigit(): # Clear the number we are tracking
                current_num_start = None
                current_num = ""
            if char.isdigit():
                if current_num_start != None:
                    # We are looking at a number
                    current_num += char # update our current number
                    for i in range(current_num_start, char_idx + 1): # backfill all indexes
                        char_matrix[row_idx][i] = current_num
                else:
                    current_num_start = char_idx
                    char_matrix[row_idx][char_idx] = char
                    current_num = char
                continue

    return char_matrix
    
def get_parts(in_str: list[str]):
    char_matrix = create_matrix(in_str)
    parts = []
    gear_ratios = []

    row_idx = 0
    while row_idx < len(char_matrix):
        is_checking_digit = False
        row = char_matrix[row_idx]
        char_idx = 0
        while char_idx < len(row):
            char = row[char_idx]
            if char.isdigit():
                neighbors = get_neighbors(char_matrix, (row_idx, char_idx))
                # Look for neighbors that are symbols
                symbols_neighbors = filter(lambda x:is_symbol(x),neighbors)
                if len(list(symbols_neighbors)) >= 1:
                    if len(parts) == 0 or parts[-1] != char or (parts[-1] == char and is_checking_digit == False):
                        # We've already seen this digit do nothing
                        parts.append(char)                    
                else:
                    pass
                    # print("no neighbors: ", char, row_idx)
                is_checking_digit = True
            else:
                if is_asterisk(char):
                    neighbors = get_neighbors(char_matrix, (row_idx, char_idx))
                    neighbors = set(list(filter(lambda x:x.isdigit(),neighbors)))
                    if len(neighbors) == 2:
                        print(neighbors)
                        gear_ratios.append(int(list(neighbors)[0])*int(list(neighbors)[1]))
                is_checking_digit = False
            char_idx += 1
        row_idx += 1
    # print(gear_ratios)
    return parts, gear_ratios

def get_sum(parts):
    sum = 0
    for i in parts:
        sum += int(i)
    return sum

def get_gear_ratios_sum(file_content):
    sum = 0
    return sum

if __name__ == '__main__':
    file_content = read_file("input.txt")
    parts, gear_ratios = get_parts(file_content)
    sum = get_sum(parts)
    gear_sum = get_sum(gear_ratios)
    print(gear_sum)