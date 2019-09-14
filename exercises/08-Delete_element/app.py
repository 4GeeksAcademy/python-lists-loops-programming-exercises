people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    filtered_people = []
    for p in people:
        if p != person_name:
            filtered_people.append(p)

    return filtered_people

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))


