# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below
print(my_list)
for i in range(1,11):
    my_list.append(random.randint(101,201))
    i+=1
print(my_list)
