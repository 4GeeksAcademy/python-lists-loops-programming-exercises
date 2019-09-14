people = [
	{ "name": 'Joe', "birthDate": (1986,10,24) },
	{ "name": 'Bob', "birthDate": (1975,5,24) },
	{ "name": 'Erika', "birthDate": (1989,6,12) },
	{ "name": 'Dylan', "birthDate": (1999,12,14) },
	{ "name": 'Steve', "birthDate": (2003,4,24) }
]


from datetime import date
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda x: "Hello my name is " + str(x["name"]) + " and I am " + str(calculateAge(date(int(x["birthDate"])))) + " years old", people))


print(str(name_list))