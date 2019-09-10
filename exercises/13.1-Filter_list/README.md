#`13.1` Filter list

this is another example using filter list in python

For example, this algorithm filters the allNumbers list and returns a new list with only the odds numbers:

```py
allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

result = filter(lambda x: x % 2 > 0, allNumbers)
return_list = set(result)
print(return_list)
```



#📝Instructions
1. Complete the code to make it fill the resultingNames list with only the names that start with letter R
2. Use the filter function

<!-- 💡Hint:
Here is a 2:29min video explaining array.filter
https://www.youtube.com/watch?v=0qsFDFC2oEE -->