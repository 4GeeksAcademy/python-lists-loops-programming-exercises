all_numbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]


def filter_function(item):
    # Update here
    if item > 10:
        return item
    
    
greater_than_ten = list(filter(filter_function, all_numbers))

print(greater_than_ten)
