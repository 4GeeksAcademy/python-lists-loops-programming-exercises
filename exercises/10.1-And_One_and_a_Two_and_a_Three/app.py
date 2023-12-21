contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}

# Your code here
keys = list(contact.keys())
values = list(contact.values())
i = 0

for key in keys:
    print(key + ': ' + values[i])
    i = i + 1
