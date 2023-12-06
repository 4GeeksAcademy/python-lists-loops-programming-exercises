# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below

for item in range(10):
    random_integer = random.randint(1, 100)
    my_list.append(random_integer)

print(my_list)
