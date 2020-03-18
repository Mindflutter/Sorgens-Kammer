""" Print all diagonals of a given square matrix """

matrix = [[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 10, 11],
          [12, 13, 14, 15]]
# matrix = [[1, 2], [3, 4]]

print(matrix)
N = len(matrix)

# helper counter
counter = 1
for i in range(N):
    diagonal = []
    for j in range(counter):
        diagonal.append(matrix[i][j])
        i -= 1
    print(f'Diagonal: {diagonal}')
    counter += 1

# helper counter again
counter = 0
for j in range(1, N):
    diagonal = []
    for i in range(N - 1, counter, -1):
        diagonal.append(matrix[i][j])
        j += 1
    print(f'Diagonal: {diagonal}')
    counter += 1
