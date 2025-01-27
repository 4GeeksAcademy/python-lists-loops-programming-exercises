my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list=[]

for each in my_list:
    if type(each) == dict or type(each) == list:
        new_list.append(each)

print (new_list)        