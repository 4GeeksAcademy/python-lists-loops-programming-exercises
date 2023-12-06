my_list = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]

def my_function(numbers):
    new_list = []
    for i in numbers:
        # The magic happens here
        if (i == 0):
            new_list.append("Yahoo")
        elif(i == 1):
            new_list.append(1)
            
    return new_list
    
print(my_function(my_list))
