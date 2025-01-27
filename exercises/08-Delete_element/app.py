people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    new_list=[]
    for each in people:
        if each != person_name:
            new_list.append(each)
    return new_list
    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
