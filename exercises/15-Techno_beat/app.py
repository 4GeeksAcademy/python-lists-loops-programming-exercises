def lyrics_generator(numbers):
    zero = []
    for x in numbers:
        if x == 1:
            zero.append("Drop the base")
        elif x == 0:
            zero.append("boom")
    return zero

print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))