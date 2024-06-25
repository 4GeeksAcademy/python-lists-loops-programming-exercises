the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def booleanos(bool):
    if bool == 0:
        return 'woko'
    else: 
        return 'wiki'

print(list(map(booleanos,the_bools)))