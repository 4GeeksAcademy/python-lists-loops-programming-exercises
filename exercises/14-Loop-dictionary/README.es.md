# `14` Loop a Dictionary

Puedes pensar en un diccionario como en una lista con posiciones no numéricas:

```python
list = ["a","b","c"]
dictionary = { "one": "a", "two": "b", "three": "c"}
```

## Cómo obtener valores de un diccionario (muy similar a las listas):

```python
person = { "name": "Juan", "lastname": "Contreras" }
print(person["name"]) # Salida: "Juan"
```

## Cómo añadirle un nuevo valor a un diccionario:

```python
person["age"] = 22
print(person) # Salida: { "name": "Juan", "lastname": "Contreras", "age": 22 }
```

Para hacerle un bucle en una lista, puedes hacer lo siguiente:

```python
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

for key in spanish_translations:
    print(key) # <- salida: "dog",  "house", "cat"
    print(spanish_translations[key]) # <- salida: "perro",  "casa", "gato"
```

## 📝Instrucciones:

1. Añade programáticamente las siguientes traducciones al diccionario `spanish_translations`:

```txt
love -> amor
code -> codigo
smart -> inteligente
```
