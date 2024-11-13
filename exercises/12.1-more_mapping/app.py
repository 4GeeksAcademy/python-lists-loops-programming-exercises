my_numbers = [23,234,345,4356234,243,43,56,2]

# Your code here
# new_list = []
def multiply_by_three(num):
    return num*3

new_list = list(map(multiply_by_three, my_numbers))
print(new_list)
