the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def wiki_woko(the_bit):
    if the_bit ==1 :
        return "wiki"
    else:
        return "woko"

new_list = list(map(wiki_woko,the_bools))
print(new_list)

