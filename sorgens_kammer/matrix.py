test_matrix = [
    [1, 3, 6, 10],
    [2, 5, 9, 13],
    [4, 8, 12, 15],
    [7, 11, 14, 16]
]


def print_diag(matrix):
    """ """
    size = len(matrix[0])
    for i in range(size):
        h = i
        for j in range(h + 1):
            print(matrix[h][j])
            h -= 1
    print('half')
    for i in reversed(range(1, size)):
        h = size - 1
        for j in range(i):
            print(matrix[h][size - i + j])
            h -= 1


print_diag(test_matrix)

main_diag = [test_matrix[i][i] for i in range(4)]
other_diag = [test_matrix[i][j] for i, j in enumerate(reversed(range(4)))]

print(main_diag, other_diag)
