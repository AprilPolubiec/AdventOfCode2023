
import os

def read_file(filename: str):
    print(os.path.dirname(os.path.realpath(__file__)))
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r") as f:
        lines = f.readlines()
    return lines

def is_symbol(c: str):
    return c is not None and not c.isdigit() and not c == "."

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

def get_parts(in_str: list[str]):
    char_matrix = [ [c for c in l] for l in in_str ]
    parts = []
    for row_idx in range(len(char_matrix)):
        row = char_matrix[row_idx]
        curr_digit = ""
        found_neighbor = False
        for char_idx in range(len(row)):
            char = row[char_idx]
            if not char.isdigit() and curr_digit != "":
                if found_neighbor:
                    parts.append(curr_digit)
                    found_neighbor = False
                curr_digit = ""
                continue
            if char.isdigit():
                curr_digit += char
                neighbors = get_neighbors(char_matrix, (row_idx, char_idx))
                # Look for neighbors that are symbols
                for neighbor in neighbors:
                    if is_symbol(neighbor):
                        found_neighbor = True
                        continue
        if curr_digit != "" and found_neighbor:
            parts.append(curr_digit)
    return parts

def get_sum(parts):
    sum = 0
    for i in parts:
        sum += int(i)
    return sum

if __name__ == '__main__':
    file_content = read_file("input.txt")
    res = get_parts(file_content)
    # print(res)
    sum = get_sum(res)
    print(sum)