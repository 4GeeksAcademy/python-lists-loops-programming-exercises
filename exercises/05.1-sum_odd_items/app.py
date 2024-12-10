my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds():
    result = 0
    for i in range(0,len(my_list)):
        if (my_list[i] % 2 != 0):
            result += my_list[i]

    print(result)
    return result
sum_odds()