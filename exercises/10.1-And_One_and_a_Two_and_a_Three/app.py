contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}

# Your code here
for i in range(0,len(contact)):
    print(list(contact.keys())[i]+": "+list(contact.values())[i])
# Solution
#for key in contact.keys():
#    print(f"{key}: {contact[key]}")

