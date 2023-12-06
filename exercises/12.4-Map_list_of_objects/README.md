# `12.4` Map a list of dictionaries

The most common scenario for the mapping function is simplifying given lists, for example:

The current algorithm creates a list with only the names of the people and prints it on the console.

## 📝 Instructions:

1. At this time, the function `format_greeting` is printing the names only. Please update the mapping function so it creates a list where each item contains the following:

```py
'Hello, my name is <name> and I am <age> years old'
```

## 💡 Hints:

+ You have to get the age of each person based on their `birth_date`.

+ Take your time to understand the already defined `calculate_age` function.

+ Search in Google "How to get the age of a given birth date in python".

+ Inside your `format_greeting` function you have to return a concatenation.

## 💻 Expected result:

The result should be similar to this, but the ages might be different.

```py
[ 'Hello, my name is Joe and I am 32 years old',
  'Hello, my name is Bob and I am 42 years old',
  'Hello, my name is Erika and I am 28 years old',
  'Hello, my name is Dylan and I am 18 years old',
  'Hello, my name is Steve and I am 14 years old' ]
```
