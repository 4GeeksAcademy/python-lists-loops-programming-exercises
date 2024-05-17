the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def cambiar_valores(valor):
       if valor == 0:
        return "woko"
       else:
        return "wiki"

new_list = list(map(cambiar_valores, the_bools))

print(new_list)
