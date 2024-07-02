# Your code here
def matrix_builder(num):
    matrix = []
    
    for i in range(num):
        lista1 = []
        for j in range(num):
            lista1.append(1)
        matrix.append(lista1)
    return matrix

print(matrix_builder(3))