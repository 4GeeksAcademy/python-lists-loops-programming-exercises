#`13.1` Filter list

this is another example using filter list in python

For example, this algorithm filters the allNumbers list and returns
 a new list with only the odds numbers:

```py
allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

def myFunction(numb):
    return numb % 2 == 0

oddNumbers = list(filter(myFunction, allNumbers))
print(oddNumbers)
```



#📝Instructions
1. Complete the code to make it fill the resultingNames list with only the names that start with letter R
2. Use the filter function

```py
The console expected:
['Romario', 'Roosevelt']
```