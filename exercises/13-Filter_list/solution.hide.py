all_numbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]


def filter_function(item):
    # Update here
    return item > 10
    
greater_than_ten = list(filter(filter_function, all_numbers))

print(greater_than_ten)
