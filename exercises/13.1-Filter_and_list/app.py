all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def filtar(param):
    if param[0] == 'R':
        return param

resulting_names = list(filter(filtar, all_names))

print(resulting_names)




