celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius):
    # The magic happens here
   return (celsius * 9/5) + 32

result = list(map(celsius_to_fahrenheit, celsius_values))

print(result)
