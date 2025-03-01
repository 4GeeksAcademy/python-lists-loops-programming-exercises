# Your code here
def matrix_builder(n):
    matrix = []
    cols = n
    rows = n
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(1)
        matrix.append(row)
    return matrix
print(matrix_builder(2))