Celsius_values = [-2,34,56,-10]

result = map(lambda x : x * 5 / 9 + 32, Celsius_values)
fahrenheit_values = set(result)
print(fahrenheit_values)




def fahrenheit_values(x):
    return x * 5/9 + 32
Celsius_values = [-2,34,56,-10]
result = map(fahrenheit_values, Celsius_values)
total = set(result)
print(total)
