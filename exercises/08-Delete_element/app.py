people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    aux_people = []
    for i in people:
        if person_name != i:
            aux_people.append(i)
        #aux_people.append(i)
        #if(person_name in aux_people):
        #    aux_people.remove(person_name)
    return aux_people

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
