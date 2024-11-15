def lyrics_generator(list):
    beats = ["Boom", "Drop the bass", "!!!Break the bass!!!"]
    final_beat = []
    break_the_bass = 0
    for i in list:
        if i == 1:
            final_beat.append(beats[1])
            break_the_bass += 1
            if break_the_bass == 3:
                final_beat.append(beats[2])
        elif i == 0: 
            final_beat.append(beats[0])
            break_the_bass = 0
    return " ".join(final_beat)+" "


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
