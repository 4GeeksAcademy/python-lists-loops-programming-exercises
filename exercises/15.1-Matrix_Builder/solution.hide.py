# Your code here
def matrix_builder(n):
    matrix = [] 

    for i in range(n):
        row = []
        for j in range(n):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrix_builder(3)

print(result)
