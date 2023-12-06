def lyrics_generator(input_list):
    lyrics = ""
    count = 0

    for num in input_list:
        if num == 0:
            lyrics += "Boom "
            count = 0
        elif num == 1:
            lyrics += "Drop the bass "
            count += 1

            if count == 3:
                lyrics += "!!!Break the bass!!! "
                count = 0

    return lyrics

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
