celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius):
    # The magic happens here  
    fahrenheit_values = [(celsius * 9/5) + 32 for celsius in celsius_values]    
    return fahrenheit_values


    
    
result = list(map(celsius_to_fahrenheit, celsius_values))  
print(celsius_to_fahrenheit(celsius_values))
