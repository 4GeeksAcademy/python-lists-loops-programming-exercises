# Your code here
def matrix_builder(n):
    return [[1 for _ in range(n)] for _ in range(n)]

# El return de arriba es equivalente a escribir:
# resultado = []
# for _ in range(n):
#     resultado.append(1)


print(matrix_builder(5))