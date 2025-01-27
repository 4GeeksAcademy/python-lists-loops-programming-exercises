the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def convert(number):
    if number == 1:
        value = "wiki"
    if number == 0:
        value = "woko"
    return value


converted_list = list(map(convert,the_bools))
print(converted_list)