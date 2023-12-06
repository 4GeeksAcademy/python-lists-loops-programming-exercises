# `12.1` More mapping

The `map()` method calls a function for each value in a list and then outputs a new list with the modified values.

```py
def increment_by_one(number):
    return number + 1

my_list = [1, 2, 3, 4]
result = map(increment_by_one, my_list)  # returns [2, 3, 4, 5]
```

## 📝 Instructions:

1. Create a function named `multiply_by_three` that will multiply each number by 3.

2. Use the list `map()` function to run the `multiply_by_three` function through each value in the list.

3. Store the new list in a variable named `new_list` and `print()` the new values.

## 💡 Hints:

+ The `map()` function will apply the specified function to every item in your list.

+ Remember to store your result in the `new_list`.
