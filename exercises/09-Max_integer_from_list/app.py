my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code here:
"""the function it's not here, the student has to create the function from 0 to the end"""

max_integer = my_list[0]
for i in my_list:
    if i > max_integer:
        max_integer = i
print(max_integer)


for i in range(len(my_list)):
    if my_list[i] > max_integer:
        max_integer.append(my_list[i])
print(max_integer)