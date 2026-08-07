my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(my_list):
    max_value = my_list[0]
    for i in my_list: 
       if (i > max_value):
           max_value = i

    return max_value




print(max_integer(my_list))