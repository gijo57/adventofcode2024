import numpy as np

with open('input.txt') as f:
    word_search = np.array([list(line.strip()) for line in f.readlines()])


def check_horizontal(word_search):
    xmas_count = 0
    for row_i in range(len(word_search)):
        row = word_search[row_i]

        for col_i in range(len(row)-3):
            char1 = word_search[row_i, col_i]
            char2 = word_search[row_i, col_i+1]
            char3 = word_search[row_i, col_i+2]
            char4 = word_search[row_i, col_i+3]
            string = char1 + char2 + char3 + char4
            if (string == 'XMAS'):
                xmas_count += 1
    return xmas_count


def check_diagonal(word_search):
    xmas_count = 0

    for row_i in range(len(word_search)-3):
        row = word_search[row_i]
        for col_i in range(len(row)-3):
            char1 = word_search[row_i, col_i]
            char2 = word_search[row_i+1, col_i+1]
            char3 = word_search[row_i+2, col_i+2]
            char4 = word_search[row_i+3, col_i+3]
            string = char1 + char2 + char3 + char4
            if (string == 'XMAS'):
                xmas_count += 1
    return xmas_count


def count_xmas(word_search):
    xmas_count = 0
    xmas_count += check_horizontal(word_search)
    xmas_count += check_horizontal(np.rot90(word_search))
    xmas_count += check_horizontal(np.rot90(word_search, k=2))
    xmas_count += check_horizontal(np.rot90(word_search, k=3))
    xmas_count += check_diagonal(word_search)
    xmas_count += check_diagonal(np.rot90(word_search))
    xmas_count += check_diagonal(np.rot90(word_search, k=2))
    xmas_count += check_diagonal(np.rot90(word_search, k=3))

    return xmas_count


def count_x_mas(word_search):
    x_mas_count = 0

    corner_dict = {
        'M': 'S',
        'S': 'M'
    }

    for row_i in range(1, len(word_search)-1):
        row = word_search[row_i]

        for col_i in range(1, len(row)-1):
            char = word_search[row_i, col_i]

            if (char == 'A'):
                left_up = word_search[row_i-1, col_i-1]
                right_up = word_search[row_i-1, col_i+1]
                left_down = word_search[row_i+1, col_i-1]
                right_down = word_search[row_i+1, col_i+1]

                if (left_up == 'X' or right_up == 'X' or left_down == 'X' or right_down == 'X'):
                    continue
                elif (left_up == 'A' or right_up == 'A' or left_down == 'A' or right_down == 'A'):
                    continue
                else:
                    if (right_down == corner_dict[left_up] and left_down == corner_dict[right_up]):
                        x_mas_count += 1

    return x_mas_count


answer1 = count_xmas(word_search)
answer2 = count_x_mas(word_search)
print(answer1, answer2)