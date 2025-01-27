# Your code here
matrix=[]

def matrix_builder(x):
    matrix=[]

    for first in range(x):
        row = []
        for second in range(x):
            row.append(1)
        matrix.append(row)
    return matrix

print(matrix_builder(5))