
def lyrics_generator(list1):

    lyricStr =""
    countOnes = 0

    for item in list1:
        if item==0:
            lyricStr += "Boom "
            countOnes = 0       
        else: 
            lyricStr +="Drop the bass "         
            countOnes +=1
            if countOnes ==3:
              lyricStr += "!!!Break the bass!!! "
              countOnes = 0        
    return lyricStr


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
