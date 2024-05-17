chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    lista_conjunta = []
    for nombre in list1:
        lista_conjunta.append(nombre)
    for nombre in list2:
        lista_conjunta.append(nombre)
    return lista_conjunta
    
print(merge_list(chunk_one, chunk_two))
