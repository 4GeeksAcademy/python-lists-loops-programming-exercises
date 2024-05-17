my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here

new_list = []

for elemento in my_list:
    if type(elemento) == dict or type(elemento) == list:
        new_list.append(elemento)
        
print(new_list)



