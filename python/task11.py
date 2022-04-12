from functools import reduce

with open("./inc/task11.txt", "r") as f:
    numbers = f.read().strip().split('\n')
    numbers = [list(map(int, row.strip().split(' '))) for row in numbers]

def largestProductInGrid(matrix) -> int:
    largest = 0

    for i in matrix:
        multiple = reduce(lambda x,y: x*y, i)
        if multiple > largest:
            largest = multiple
    for j in range(len(matrix)):
        multiple = 1
        for k in range(len(matrix)):
            multiple *= matrix[k][j]
        if multiple > largest:
            largest = multiple

    multiple = 1
    rightDiagonal = 1

    for k in range(len(matrix)):
        multiple *= matrix[k][k]
        rightDiagonal *= matrix[len(matrix)-1-k][k]
    if multiple > largest:
        largest = multiple
    if rightDiagonal > largest:
        largest = rightDiagonal

    return largest

matrix = []

for i in range(len(numbers) - 3):
    for j in range(len(numbers[0]) - 3):
        subMatrix = []
        subMatrix.append(numbers[i][j:j+4])
        subMatrix.append(numbers[i+1][j:j+4])
        subMatrix.append(numbers[i+2][j:j+4])
        subMatrix.append(numbers[i+3][j:j+4])
        matrix.append(subMatrix)

matrix = map(largestProductInGrid, matrix)

print(max(matrix))

    
