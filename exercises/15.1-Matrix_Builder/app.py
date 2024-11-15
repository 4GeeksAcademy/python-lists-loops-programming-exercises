# Your code here
def matrix_builder(num):
    matrix = []
    matrix_sub = []
    for i in range(num):
        for j in range(num):
            matrix_sub.append(1)
        matrix.append(matrix_sub)
        matrix_sub = []
    return matrix

print(matrix_builder(5))