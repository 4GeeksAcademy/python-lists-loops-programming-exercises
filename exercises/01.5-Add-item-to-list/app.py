# Remember to import random function here
import random
my_list = [4, 5, 734, 43, 45]

# The magic goes below
for i in range(0,10):
    numero_random = random.randint(0,100)
    new_list = my_list.append(numero_random)

print(new_list)