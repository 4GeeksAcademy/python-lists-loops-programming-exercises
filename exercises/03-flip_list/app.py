sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list= []

# new_list =sample_list.reverse()
# print(sample_list)

# for index, item in enumerate(sample_list):
#     new_list[index]=item
new_list_index = 0
for i in range(len(sample_list)-1,-1,-1):
    new_list.insert(new_list_index,sample_list[i])
    new_list_index +=1
print (new_list)