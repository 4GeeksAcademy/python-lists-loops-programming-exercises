the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def wiki_woko(number):
    if number == 1:
        return "wiki"
    elif number == 0:
        return "woko"

print(list(map(wiki_woko, the_bools)))