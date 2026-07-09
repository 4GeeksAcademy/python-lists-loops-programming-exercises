def lyrics_generator(beats):
    result = []
    count_ones = 0

    for beat in beats:
        if beat == 0:
            result.append("Boom")
            count_ones = 0
        elif beat == 1:
            result.append("Drop the bass")
            count_ones += 1
            if count_ones == 3:
                result.append("!!!Break the bass!!!")
                count_ones = 0
    print(" ".join(result) + " ")  


# Your code above, nothing to change after this line
lyrics_generator([0,0,1,1,0,0,0])
lyrics_generator([0,0,1,1,1,0,0,0])
lyrics_generator([0,0,0])
lyrics_generator([1,0,1])
lyrics_generator([1,1,1])
# Terminado