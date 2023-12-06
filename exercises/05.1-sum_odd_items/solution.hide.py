my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    odd_sum = 0

    for num in list:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum

print(sum_odds(my_list))
