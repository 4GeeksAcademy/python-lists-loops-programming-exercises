sample_list = [45, 67, 87, 23, 5, 32, 60]
new_list=[]

# Your code below
for each in range(len(sample_list)-1,-1,-1):
    new_list.append(sample_list[each])

print(new_list)