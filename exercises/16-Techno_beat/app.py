
def lyrics_generator(beats):
    the_tune = ""
    counter=0
    for i in beats:
        if i == 0:
            the_tune += "Boom "
            count=0
        elif i == 1:
            the_tune += "Drop the bass "
            counter += 1
            if counter == 3:
                the_tune += "!!!Break the bass!!!"
                counter=0

    return the_tune


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
