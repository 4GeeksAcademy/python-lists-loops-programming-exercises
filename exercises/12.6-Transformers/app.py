incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#return the dict into the list
all_people = list(map(lambda p: p["name"] + " " + p["lastName"], incomingAJAXData))
print(all_people)

#function return dict into the list
def my_function(items):
    return items['name'] +' '+items['lastName']

result = list(map(my_function, incomingAJAXData))
sample = set(result)
print(sample)
