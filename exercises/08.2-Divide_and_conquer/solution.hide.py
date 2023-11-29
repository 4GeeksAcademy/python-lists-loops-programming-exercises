list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(numbers):
    odd = []
    even = []

    for i in numbers:
        if (i % 2 == 1):
            odd.append(i)
        elif (i % 2 == 0):
            even.append(i)

    sorted_numbers = [odd, even]
    
    return sorted_numbers

print(sort_odd_even(list_of_numbers))
