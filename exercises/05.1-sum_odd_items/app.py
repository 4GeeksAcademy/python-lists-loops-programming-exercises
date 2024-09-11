my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(item):
    odd_numbers = 0
    for item in my_list:
        if item % 2 != 0:
            odd_numbers += item   
    return odd_numbers

print(sum_odds(my_list))