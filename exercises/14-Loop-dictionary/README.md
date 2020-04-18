# `14` Loop A Dictionary

You can think of a dictionary like a list with non-numerical positions:

```python
list = ["a","b","c"]
dictionary = { "one": "a", "two": "b", "three": "c"}
```

![Python list vs dict](https://ucarecdn.com/4671e04e-651d-4434-a01a-f019dddfb2d2/)

## Retrieve dictonary values (very similar to lists)

```python
person = { "name": "Juan", "lastname": "Contreras" }
print(person["name"]) # Output: "Juan"
```

## Add new value to dictionary

```python
person["age"] = 22
print(person) # Output: { "name": "Juan", "lastname": "Contreras", "age": 22 }

```

In order to loop a list you can do:

```python
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

for key in spanish_translations:
    print(key) # <- output: "dog",  "house", "cat"
    print(spanish_translations[key]) # <- output: "perro",  "casa", "gato"
```

# 📝Instructions

Programatically add the following translations to the `spanish_translations` dictionary:

```txt
love -> amor
code -> codigo
smart -> inteligente
```
