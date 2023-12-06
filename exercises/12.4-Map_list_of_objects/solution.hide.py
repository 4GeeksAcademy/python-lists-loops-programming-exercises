import datetime

people = [
	{ "name": 'Joe', "birth_date": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birth_date": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birth_date": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birth_date": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birth_date": datetime.datetime(2003,4,24) }
]

def calculate_age(date_of_birth):
    today = datetime.date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age

def format_greeting(person):
    # Your code here
    name = person["name"]
    age = calculate_age(person["birth_date"])
    return f"Hello, my name is {name} and I am {age} years old"

name_list = list(map(format_greeting, people))

print(name_list)
