my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list = []
for i in my_list:
    if (type(i) == dict) or (type(i) == list):
        
        new_list.append(i)
print(new_list)
