# `14` Loop A Dictionary

The dictionaries allow us to identify each element by a `key`, opposed to lists where there are only values and indexes. To define a dictionary, the list of values is enclosed in curly braces. Key and value pairs are separated by commas, and keys are separated from values by colons: 

```py
{
    "key": value,
    "other_key": other_value,
    ...
}
```

### You can think of a dictionary like a list with non-numerical positions:

```python
list = ["a", "b", "c"]
dictionary = { "one": "a", "two": "b", "three": "c" }
```

### How to retrieve dictionary values (very similar to lists):

```python
person = { "name": "Juan", "lastname": "Contreras" }
print(person["name"])  # Output: "Juan"
```

### How to add a new value to the dictionary:

```python
person["age"] = 22
print(person)  # Output: { "name": "Juan", "lastname": "Contreras", "age": 22 }
```

### In order to loop a dictionary, you can do:

```python
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

for key in spanish_translations:
    print(key)  # <-- Output: "dog", "house", "cat"
    print(spanish_translations[key])  # <-- Output: "perro", "casa", "gato"
```

## 📝 Instructions:

1. Programmatically add the following translations to the `spanish_translations` dictionary:

```txt
love -> amor
code -> codigo
smart -> inteligente
```

## 💻 Expected output:

```py
{'dog': 'perro', 'house': 'casa', 'cat': 'gato', 'love': 'amor', 'code': 'codigo', 'smart': 'inteligente'}
```
