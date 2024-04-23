the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def waka(list):
    if list==0:
        return 'woko'
    else: return 'wiki'

new_list= list(map(waka, the_bools))

print(new_list)