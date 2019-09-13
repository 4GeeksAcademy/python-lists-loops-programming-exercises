arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:


new_list = []
for numb in range(len(arr)):
    new_list.append(arr[-(numb+1)])
print(new_list)
