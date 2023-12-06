# `08.2` Divide and conquer

## 📝 Instructions:

1. Create a function called `sort_odd_even` that expects a list of numbers (integers).

2. Loop through the list and separate the *odd* and the *even* numbers.

3. Create a variable called `sorted_list` to start appending the *odd* numbers.

4. If the number is even, push it to a placeholder list named `even`.

5. Then insert the `even` list into the `sorted_list`. Remember, the *odd* numbers come first, and you have to insert the `even` list after.

## 💡 Hints:

+ Create empty (placeholder) variables when you need to store data.

+ Check out the `extend()` method: https://www.w3schools.com/python/ref_list_extend.asp

## 💻 Expected result:

Everything should be inside a single list; there should not be nested lists.

```py
sort_odd_even([1, 2, 33, 10, 20, 4])

[1, 33, 2, 10, 20, 4] # <-- Yes
[[1,33], [2,10,20,4]] # <-- No
```
