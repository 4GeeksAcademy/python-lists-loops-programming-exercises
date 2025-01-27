my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

# Your code here
counter=0
total=0

for each in my_list:
    counter += 1
    total += each

avg = total/counter

print(avg)

average = sum(my_list)/len(my_list)
print(average)
