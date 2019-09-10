
def my_function(items):
     return type(items)

list_of_Strings = ['1','5','45','34','343','34',6556,323]
result = map(my_function,  list_of_Strings)
sample = set(result)
print(sample)


#this return the same
list_of_Strings = ['1','5','45','34','343','34',6556,323]
other = map(lambda item: type(item), list_of_Strings)
sample = set(other)
print(sample)

