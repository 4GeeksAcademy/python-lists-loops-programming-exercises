list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list):
    sorted_list=[]
    even=[]

    for each in list:
        if each % 2 != 0:
            sorted_list.append(each)
        else:
            even.append(each)
    
    sorted_list.extend(even)

    return sorted_list

print(sort_odd_even(list_of_numbers))

