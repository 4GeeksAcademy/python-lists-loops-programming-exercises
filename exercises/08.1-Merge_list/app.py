chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    merge = []
    for i in list1:
        i += i
        for j in list2:
            j += j
            merge = list1 + list2

    return merge
print(merge_list(chunk_one, chunk_two))
