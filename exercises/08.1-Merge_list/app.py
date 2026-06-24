chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    merged_list = []
    # same as "spread operator '...' in JavaScript"
    # here we use '*' to unpack the lists and tuples, and use '**' to unpack dictionaries
    # merged_list = [*list1,*list2]
    merged_list = [*list1]
    for item in list2:
        merged_list.append(item)
    return merged_list
    
print(merge_list(chunk_one, chunk_two))
