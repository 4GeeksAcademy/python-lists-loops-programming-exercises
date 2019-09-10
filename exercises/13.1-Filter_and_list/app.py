#using lambda
allNames = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

result = filter(lambda x: x.startswith("R"), allNames)
return_list = set(result)
print(return_list)
