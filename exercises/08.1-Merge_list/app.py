chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    final_list = []
    for i in list1:
        final_list.append(i)
    for i in list2:
        final_list.append(i)
    
    return final_list
    
print(merge_list(chunk_one, chunk_two))
