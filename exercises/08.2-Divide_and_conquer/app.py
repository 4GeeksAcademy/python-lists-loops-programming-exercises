list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:


odd_number = []
even_number = []
def merge_two_list(items):
    for i in items:
        if i % 2 != 0:
            odd_number.append(i)
            i += i
        else:
            even_number.append(i)
    return odd_number + even_number
print(merge_two_list(list_of_numbers))