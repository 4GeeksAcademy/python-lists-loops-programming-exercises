mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below
def getTypeOfElements(myList):

    for i in range(0,len(myList),1):
        myList[i] = type(myList[i])    
    return myList

newArr = getTypeOfElements(mix)

for x in newArr:
    print(x)
