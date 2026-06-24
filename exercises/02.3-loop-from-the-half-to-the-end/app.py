my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# Your code here
inicial_value = len(my_list) // 2
stop_value = len(my_list)
increase_value = 1

for i in range(inicial_value, stop_value, increase_value):
    print(my_list[i])
