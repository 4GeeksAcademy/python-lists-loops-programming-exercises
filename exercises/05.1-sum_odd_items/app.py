my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    lista_impares = 0

    for numero in list:
        if numero % 2 != 0:
           lista_impares += numero
    return lista_impares

print(sum_odds(my_list))
