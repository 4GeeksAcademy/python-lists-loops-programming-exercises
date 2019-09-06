arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:

for i in range(len(arr)):
    print(arr[-(i+1)])


for i in range(len(arr)):
    print(arr[-i-1])