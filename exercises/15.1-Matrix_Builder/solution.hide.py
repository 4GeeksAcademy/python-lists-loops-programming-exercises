# Your code here
def matrix_builder(n):
    matrix = [] 

    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrix_builder(6)

print(result)
