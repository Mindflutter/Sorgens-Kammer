def secondary_diagonals(matrix):
    """ Prints all secondary diagonals of a given square matrix """
    size = len(matrix[0])
    for i in range(size):
        h = i
        diagonal = []
        for j in range(h + 1):
            diagonal.append(matrix[h][j])
            h -= 1
        print(f"Diagonal: {diagonal}")

    for i in reversed(range(1, size)):
        h = size - 1
        diagonal = []
        for j in range(i):
            diagonal.append(matrix[h][size - i + j])
            h -= 1
        print(f"Diagonal: {diagonal}")


def longest_diagonals(matrix):
    """ Print longest diagonals, one-liner approach """
    size = len(matrix[0])
    main_diagonal = [matrix[i][i] for i in range(size)]
    secondary_diagonal = [matrix[i][j] for i, j in enumerate(reversed(range(size)))]
    print(f"Longest main: {main_diagonal}, Longest secondary: {secondary_diagonal}")


def secondary_diagonals_2(matrix):
    """ Prints all secondary diagonals of a given square matrix """
    size = len(matrix[0])
    # helper counter
    counter = 1
    for i in range(size):
        diagonal = []
        for j in range(counter):
            diagonal.append(matrix[i][j])
            i -= 1
        print(f"Diagonal: {diagonal}")
        counter += 1

    # helper counter again
    counter = 0
    for j in range(1, size):
        diagonal = []
        for i in range(size - 1, counter, -1):
            diagonal.append(matrix[i][j])
            j += 1
        print(f"Diagonal: {diagonal}")
        counter += 1


test_matrix = [
    [1, 3, 6, 10],
    [2, 5, 9, 13],
    [4, 8, 12, 15],
    [7, 11, 14, 16]
]

longest_diagonals(test_matrix)

# Two implementations take approximately the same time
secondary_diagonals(test_matrix)
secondary_diagonals_2(test_matrix)
