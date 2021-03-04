matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [2, 4, 6]]

matrix2 = [[5, 3, 1, 4],
          [11, 9, 8, 8],
          [0, 2, 0, 7]]

result =[[0 for i in range(len(matrix))] for j in range(len(matrix2[0]))]


for i in range(len(matrix)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix[i][k] * matrix2[k][j]


for i in result:
    print(i)

