
allNames = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]


def persons(names):
    if 'R' in names:
        return True
    else:
        return False

resultingNames = list(filter(persons, allNames))
print(resultingNames)

