my_list = [43,23,6,87,43,1,
           4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(lista):
    numero_maximo = lista[0]
    for numero in lista:
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo

print(max_integer(my_list))