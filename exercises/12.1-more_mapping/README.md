# `12.1` More mapping



The list `map` method calls a function for each value in a
list  and then outputs a new list with the modified values.

```py
#incrementByOne
def values_list(number) {
  return number + 1
}

my_list = [1, 2, 3, 4]
result = map(values_list, my_list)  #returns [2, 3, 4, 5]
```

# 📝Instructions:

1. Create a function named increment_by_one that will multiply each number by 3.
2.Pass a argument into the function
3. Use the list map() function to run the increment_by_one function through each value in the list.
4. Store the new list in a variable named total and print() the new list.

💡Hint:
The function will take a parameter with the original item being transformed and added into the new list.
Remember that your function must return each of the new items to be stored into the new list.


