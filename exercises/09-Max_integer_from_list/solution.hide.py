my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def maxInteger(arr):
    maxInt=0
    for i in range(len(arr)):
        if arr[i] > maxInt:
            maxInt = arr[i]
    return maxInt

print(maxInteger(my_list))