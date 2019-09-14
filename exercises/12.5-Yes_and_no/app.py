theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]



def other(numbers):
    if numbers == 1:
        return "wiki"
    else:
        return "woko"
result = list(map(other, theBools))
print(result)


