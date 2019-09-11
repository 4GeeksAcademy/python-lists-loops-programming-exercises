theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def other(numbers):
    if numbers == 1:
        return "wiki"
    else:
        return "woko"
result = list(map(other, theBools))
print(result)



rate = lambda x : "wiki" if (x == 1) else "woko"
sample = list(map(rate, theBools))
print(sample)
