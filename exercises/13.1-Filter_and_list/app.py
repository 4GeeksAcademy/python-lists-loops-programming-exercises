#using lambda
allNames = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

result = filter(lambda x: x.startswith("R"), allNames)
return_list = set(result)
print(return_list)


#the same result
def my_function(names):
    if 'R' in names:
        return True
    else:
        return False

my_filter_function = filter(my_function, allNames)
result = set(my_filter_function)
print(result)

