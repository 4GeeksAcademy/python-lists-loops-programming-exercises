def lyrics_generator(lyrics):
    song = ""
    aux=0
    for i in lyrics:
        if i == 0:
            song += "Boom "
        elif i == 1:
            song += "Drop the bass "
            aux += 1
            if aux == 3:
                song += "!!!Break the bass!!! "
                aux=0
    return song


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
