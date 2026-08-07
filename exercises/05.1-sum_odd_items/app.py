my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds():
    sumImpar = 0
    for i in range(0, len(my_list)):
       if my_list[i] % 2 != 0 :
            sumImpar += my_list[i] 

    return sumImpar        

print(sum_odds())