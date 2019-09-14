my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for numb in numbers:
    #The magic go here:
        # if numb == 0:
        #     new_list.append("Yahoo")
        # elif numb == 1:
        #     new_list.append(numb)
    return new_list
print(my_function(my_list))
