allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

result = filter(lambda x: x > 10, allNumbers)
total = set(result)
print(total)




#the same result
def sample(items):
    return items > 10

other_list = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]
return_list = filter(sample, other_list)
aux = set(return_list)
print(aux)