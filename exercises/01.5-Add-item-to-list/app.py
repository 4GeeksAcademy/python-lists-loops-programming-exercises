# Remember to import random function here

my_list = [4, 5, 734, 43, 45]

# The magic goes below
import random
for i in range(0,10):
    my_list.append(random.randint(0,10))
print(my_list)