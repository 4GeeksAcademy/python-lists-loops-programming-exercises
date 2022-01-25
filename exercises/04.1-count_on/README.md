# `04.1` Count On

As you saw in the last exercise your list can be a mix `types of data` we are going to divide and conquer.

Would you be so kind to add all the items with data-type `dict` and `list` into the hello list?

## 📝Instructions:

1. Loop the given list.

2. Push the data-types `dict` and `list` found to a new list called `hello`.

3. Print the variable `hello`.

## 💡 Hint :

+ Remember that you can know the data-type of a variable or value with the function `type()`.

+ Check this link for more information about the `type()` function: https://www.w3schools.com/python/ref_func_type.asp

Here is how to print ALL the items.

```py
my_list = [42, true, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

for x in my_list:
    print(x)
```

## Expected result:

```py
[[2, 1], {'name': 'juan'}]
```
