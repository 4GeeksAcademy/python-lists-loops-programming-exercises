my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    odd_numbers = 0
    for num in list:
        if num%2 != 0:
            odd_numbers += num
    return odd_numbers

print(sum_odds(my_list))
        