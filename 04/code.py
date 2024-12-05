def depth_first_search_find_string(matrix, row, col):
    if matrix[row][col] == "X":
        return (find_diagonal_up_left(matrix, row, col, "XMAS"), find_diagonal_up_right(matrix, row, col, "XMAS"), find_string_back(matrix, row, col, "XMAS"), find_string_up(matrix, row, col, "XMAS"))
    if matrix[row][col] == "S":
        return (find_diagonal_up_left(matrix, row, col, "SAMX"), find_diagonal_up_right(matrix, row, col, "SAMX"), find_string_back(matrix, row, col, "SAMX"), find_string_up(matrix, row, col, "SAMX"))

def find_diagonal_up_left(matrix, row, col, string):
    if len(string) == 0:
        return 1
    if matrix[row][col] == string[0]:
        new_string = string.replace(matrix[row][col], '')
        return find_diagonal_up_left(matrix, row-1, col-1, new_string)
    return 0

def find_diagonal_up_right(matrix, row, col, string):
    if len(string) == 0:
        return 1
    if matrix[row][col] == string[0]:
        new_string = string.replace(matrix[row][col], '')
        return find_diagonal_up_right(matrix, row-1, col+1, new_string)
    return 0

def find_string_back(matrix, row, col, string):
    if len(string) == 0:
        return 1
    if matrix[row][col] == string[0]:
        new_string = string.replace(matrix[row][col], '')
        return find_string_back(matrix, row, col-1, new_string)
    return 0

def find_string_up(matrix, row, col, string):
    if len(string) == 0:
        return 1
    if matrix[row][col] == string[0]:
        new_string = string.replace(matrix[row][col], '')
        return find_string_up(matrix, row-1, col, new_string)
    return 0

def add_padding(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    matrix.insert(0, ['.'] * (cols + 2))
    matrix.append(['.'] * (cols + 2))
    for row in matrix[1:-1]:
        row.insert(0, '.')
        row.append('.')
    return matrix

def part1(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "X" or matrix[row][col] == "S":
                found = sum(depth_first_search_find_string(matrix, row, col))
                if found > 0:
                    total += found
    return total

def part2(matrix):
    valid_set = {"S": 2, "M": 2}
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "A":
                char_count = {}
                char_count[matrix[row-1][col-1]] = char_count.get(matrix[row-1][col-1], 0) + 1
                char_count[matrix[row+1][col+1]] = char_count.get(matrix[row+1][col+1], 0) + 1
                char_count[matrix[row+1][col-1]] = char_count.get(matrix[row+1][col-1], 0) + 1
                char_count[matrix[row-1][col+1]] = char_count.get(matrix[row-1][col+1], 0) + 1
                if valid_set == char_count and matrix[row-1][col-1] != matrix[row+1][col+1]:
                    total += 1
    return total

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        matrix = [list(line.strip()) for line in file]
    padded_matrix = add_padding(matrix)
    total1 = part1(padded_matrix)
    print(total1)
    total2 = part2(padded_matrix)
    print(total2)