chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    new_list = []
    for each in list1:
        new_list.append(each)
    for each in list2:
        new_list.append(each)
    return new_list

    
print(merge_list(chunk_one, chunk_two))
