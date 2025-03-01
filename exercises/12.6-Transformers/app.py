incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here

def data_transformer(param_list):
    #name = param_list["name"]
    #lastname = param_list["last_name"]
    #return f"{name} {lastname}"
    return list(map(lambda x: f"{x['name']} {x['last_name']}", param_list))

#print(list(map(data_transformer, incoming_ajax_data)))
print(data_transformer(incoming_ajax_data))