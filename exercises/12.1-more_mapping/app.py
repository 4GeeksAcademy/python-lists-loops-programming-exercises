myNumbers = [23,234,345,4356234,243,43,56,2]


result = list(map(lambda x: x * 3, myNumbers))
print(result)



# other sample
def other_sample(x):
    return x * 3

result = list(map(other_sample, myNumbers))
print(result)
