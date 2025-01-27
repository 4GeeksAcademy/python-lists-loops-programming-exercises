my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here

def sum_odds(x): 
    sum_of_odds=0
    for each in x:
        if each % 2 != 0:
            sum_of_odds += each
    return (sum_of_odds)

print(sum_odds(my_list))