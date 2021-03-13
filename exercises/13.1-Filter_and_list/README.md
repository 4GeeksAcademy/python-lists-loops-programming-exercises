# `13.1` Filter list

This is another example using filter list in python.

For example, this algorithm filters the all_numbers list and returns
 a new list with only the odds numbers:

```py
all_numbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

def my_function(numb):
    return numb % 2 == 0

odd_numbers = list(filter(my_function, all_numbers))
print(odd_numbers)
```



# 📝Instructions
1. Complete the code to make it fill the resulting_names list with only the names that start with letter R.
2. Use the filter function.

```py
The console expected:
['Romario', 'Roosevelt']
```
