list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list1):
    even = []
    odd = []   

    for item in list1:
        if item %2 == 0:
            even.append(item)
        else:
            odd.append(item)   
    odd.extend(even)        
    return odd

print(sort_odd_even(list_of_numbers))

