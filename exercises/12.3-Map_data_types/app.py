list_of_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
        return type(items)

result = list(map(type_list, list_Strings))
print(result)


#this return the same
type_data = lambda data: (type(data))
sample = list(map(type_data, list_Strings))
print(sample)

