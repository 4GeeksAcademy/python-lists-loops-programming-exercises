# `13.1` Filter list

Aquí hay otro ejemplo donde se usa `filter()` en una lista en Python. 

Este algoritmo filtra la lista `all_numbers` y retorna una nueva lista solo con los números impares:

```py
all_numbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

def my_function(number):
    return number % 2 == 1

odd_numbers = list(filter(my_function, all_numbers))
print(odd_numbers)
```

## 📝 Instrucciones:

1. Escribe el código necesario para obtener una lista `resulting_names` solo con los nombres que empiezan con la letra "R".

2. Usa la función `filter()`.

## 💻 Resultado esperado:

```py
['Romario', 'Roosevelt']
```
