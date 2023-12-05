# `12` Map a list

The `map()` function applies a given function to each item of an "iterable" (list, tuple, etc.) and returns a list of the results.

### The syntax of map() is:

```py
map(function, iterable, ...)
```

#### map() Parameters:

**function:** passes each item of the iterable to this function.

**iterable:** iterable which is to be mapped. You can pass more than one iterable to the `map()` function.

#### Return Value from map():

The `map()` function applies to a given function and, in particular, to each item of an iterable to return a list of the results.

The returned value from `map()` (map object) then can be passed to functions like `list()` (to create a list), `set()` (to create a set) and so on.

## 📝 Instructions:

1. Using the same logic, add the needed code to convert a list of Celsius values into Fahrenheit inside the `map()` function.

## 💻 Expected result:

```py
[28.4, 93.2, 132.8, 14.0]
```
