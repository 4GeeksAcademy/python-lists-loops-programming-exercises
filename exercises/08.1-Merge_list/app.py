chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    aux_chunk = []
    #aux_chunk = list1 + list2
    #aux_chunk = [*list1,*list2]
    # combine python lists without duplicates
    #aux_chunk = list(set(list1+list2))
    for i in list1:
        aux_chunk.append(i)
    for j in list2:
        aux_chunk.append(j)
    return aux_chunk
    
print(merge_list(chunk_one, chunk_two))
