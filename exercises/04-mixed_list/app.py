mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:

for i in range(len(mix)):
    if mix[i] == i:
        i += 1
    print(type(mix[i]))


for i in range(len(mix)):
    item = mix[i]
    print(type(item))