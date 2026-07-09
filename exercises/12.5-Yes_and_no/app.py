the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def wokoWiki(value):
    return 'wiki' if value == 1 else 'woko'
    

print(list(map(wokoWiki, the_bools)))        