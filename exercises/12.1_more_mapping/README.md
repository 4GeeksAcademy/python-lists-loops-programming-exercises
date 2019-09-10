
myNumbers = [23,234,345,4356234,243,43,56,2]

result = map(lambda x: x * 3, myNumbers)
total = set(result)
print(total)



def other_sample(x):
    return x * 3

myNumbers = [23,234,345,4356234,243,43,56,2]
result = map(other_sample, myNumbers)
total = set(result)
print(total)
