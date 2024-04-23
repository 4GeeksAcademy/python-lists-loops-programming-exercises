list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list):
    odd=[] #1,3
    even=[] #0,2
    sorted_list=[]
    
    for i in list:
        if i%2==0:
            even.append(i)
        else: odd.append(i)
    
    for i in odd:
        sorted_list.append(i)
    for i in even:
        sorted_list.append(i)

    return sorted_list

print(sort_odd_even(list_of_numbers))

