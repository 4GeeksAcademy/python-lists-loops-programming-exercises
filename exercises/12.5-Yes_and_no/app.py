the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

new_list = list(map(lambda i: "wiki" if i == 1 else "woko", the_bools))
print(new_list)