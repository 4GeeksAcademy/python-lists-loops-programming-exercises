import random

def matrix_function(numbers):
    row = []
    for i in range(numbers):
        i+=i
        columns = []
        for x in range(numbers):
            x+=i
            columns.append(random.randint(0,1)*1)
        row.append(columns)
    return row
print(matrix_function(5))

#this in onle returning the 5 integer numbers into the rows and columns
# have to reviewing this