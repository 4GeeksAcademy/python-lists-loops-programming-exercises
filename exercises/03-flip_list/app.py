sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list = []

for i in range(len(sample_list), -1, -1):
    if i != 0:
        new_list.append(sample_list[i-1])
print(new_list)

