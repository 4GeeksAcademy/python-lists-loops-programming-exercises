names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name
result = map(prepender, names)
my_names = set(result)
print(my_names)
