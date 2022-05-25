import pytest

def rotate_matrix(matrix):
    idxLastRow = 0
    resultMatrix = [[0] * len(matrix[0]) for _ in range(len(matrix[0]))]

    for row in range(len(matrix)):
        tempRow = len(matrix) - 1
        for col in range(len(matrix)):
            resultMatrix[row][col] = matrix[tempRow][idxLastRow]
            tempRow -= 1
        idxLastRow += 1

    print(resultMatrix)



rotate_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])

rotate_matrix([[1,2],[3,4]])