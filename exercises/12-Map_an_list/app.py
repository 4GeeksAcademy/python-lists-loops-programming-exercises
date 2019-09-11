Celsius_values = [-2,34,56,-10]

fahrenheit_values = list(map(lambda x : x * 5 / 9 + 32, Celsius_values))
print(fahrenheit_values)




def fahrenheitValues(x):
    return x * 5/9 + 32
result = list(map(fahrenheit_values, Celsius_values))
print(result)
