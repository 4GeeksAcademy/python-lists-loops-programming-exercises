# Remember to import random function here
import random
my_list = [4, 5, 734, 43, 45]

# The magic goes below
print(len(my_list))
for x in range(10):
    my_list.append(random.randint(0,100))
print(len(my_list))