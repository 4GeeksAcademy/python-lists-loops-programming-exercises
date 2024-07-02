people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):

    # Your code here
    copia_people = list(people)

    if person_name in copia_people:
        copia_people.remove(person_name)
    
    return copia_people

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
