my_sample_list = [3423,5,4,47889,654,8,867543,23,48,5345,234,6,78,54,23,67,3,6,432,55,23,25,12]

def sum_all_values(item):
    total = 0
    # The magic happens here
    for item in my_sample_list:
        total += item
    
    return total
    
print(sum_all_values(my_sample_list))
