myNumbers = [23,234,345,4356234,243,43,56,2]


def increment_by_one(numbers):
    return numbers * 3

result = list(map(increment_by_one, myNumbers))
print(result)