def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = rotate(matrix)
print(res)
