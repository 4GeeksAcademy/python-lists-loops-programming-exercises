all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def starts_with_r(name):
    if name[0]=="R":
        return name

resulting_names = list(filter(starts_with_r,all_names))
print(resulting_names)




