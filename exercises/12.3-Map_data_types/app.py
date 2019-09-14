list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
        return type(items)

result = list(map(type_list, list_Strings))
print(result)



