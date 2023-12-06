def matrixBuilder(n):
    matrix = [] 

    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrixBuilder(3)

print(result)
