# def zeroMatrix(matrix):
#     rowsOfZeros = []
#     for row_i, row in enumerate(matrix):
#         if 0 in row:
#             rowsOfZeros.append(row_i)
#     for rowNumbers in range(len(rowsOfZeros)):
#         for matrixRow_i, matrixRow in enumerate(matrix):

def zeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    print(rows)
    print(cols)
    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix

print(zeroMatrix([
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ]))