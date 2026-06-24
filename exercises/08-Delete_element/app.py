people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name, personas):
    new_list = []
    for i in personas:
        if i != person_name:
            new_list.append(i)
    return new_list

    # Your code here
    

    
# Don't delete anything below
print(delete_person("daniella", people))
print(delete_person("juan", people))
print(delete_person("emilio", people))
