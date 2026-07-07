#2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])
print(matrix[1][2])

matrix[1][2] = 99

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
