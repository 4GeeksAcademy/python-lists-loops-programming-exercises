arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds(arr):
    oddSum = 0

    for num in arr:
        if num % 2 != 0:
            oddSum += num
    print(oddSum)

sumOdds(arr)