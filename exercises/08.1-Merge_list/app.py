chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    new_list = []
    for i in list1:
        new_list.append(i) 
    for i in list2:
        new_list.append(i)

    
    return new_list    

    
    # Your code here

    
print(merge_list(chunk_one, chunk_two))
