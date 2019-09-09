contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:

# declare and aux variable and assign the value of the key
k = contact.keys()


# loop the entire dict and concactenate the items in one output
for k, v in contact.items():
    print("{0}: {1}".format(k, v))


#another form:
x = contact.keys()

for x, e in contact.items():
    print(x, ":", e)

#loop without declaration:
for key, value in contact.items():
    print(key, ":", value)