# Your code here
def matrix_builder(num):
    matrix = []

    for i in range(num):
        row = []
        for r in range(num):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrix_builder(3)

print(result)