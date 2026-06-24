mixed_list = ['1','5','45','34','343','34',6556,323]

def type_list(items):
    items = type(items)        
    return items

new_list = list(map(type_list, mixed_list))
print(new_list)
