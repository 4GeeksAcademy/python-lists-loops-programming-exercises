# `14` Haz un bucle con un Dictionario

Puedes imaginarte a un diccionario como una lista con posiciones no numéricas:

```python
list = ["a","b","c"]
dictionary = { "one": "a", "two": "b", "three": "c"}
```

#### Acceder a los elementos de un diccionario (similar a como en las listas)

```python
person = { "name": "Juan", "lastname": "Contreras" }
print(person["name"]) # Salida: "Juan"
```

#### Añadir un elemento a un diccionario:

```python
person["age"] = 22
print(person) # Salida: { "name": "Juan", "lastname": "Contreras", "age": 22 }

```

Para hacer un bucle con un diccionario puedes hacerlo así:

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
