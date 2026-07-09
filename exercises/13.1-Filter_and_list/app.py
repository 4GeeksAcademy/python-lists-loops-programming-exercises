all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def filter_R_names(name):
    if name.startswith("R",0):
        return name

resulting_names = list(filter(filter_R_names,all_names))
print(resulting_names)




