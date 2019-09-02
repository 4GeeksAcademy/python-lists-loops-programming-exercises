#You have to import random function:
import random
#Feel happy to write the code below, good luck:

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list

my_stupid_list = generate_random_list()
the_last_one = my_stupid_list[-1]

print(the_last_one)


# my_stupid_list = []
# for i in range(1, 100):
#     my_stupid_list.append(random.randint(1,100))
#     the_last_one = my_stupid_list[-1]
# print(the_last_one)