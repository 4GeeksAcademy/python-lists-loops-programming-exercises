my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list = []
# for i , item in enumerate(my_list):
#     if(type(item) == list or type(item) == dict):
#         new_list.append(item)
# for i in range(0,len(my_list),1):
#     if (type(my_list[i]) ==list or type(my_list[i]) == dict):
#         new_list.append(my_list[i])

for i in range(0,len(my_list),1):
    if (isinstance(my_list[i],(list,dict))):
        new_list.append(my_list[i])
print(new_list)