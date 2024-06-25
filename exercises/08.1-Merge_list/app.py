chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(lista1, lista2):
    # Your code here
    nueva_lista = []
    for i in lista1:
        nueva_lista.append(i)
    for i in lista2:
        nueva_lista.append(i)

    return nueva_lista

    
print(merge_list(chunk_one, chunk_two))
