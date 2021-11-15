# `13.1` Filtrar Listas

Aquí hay otro ejemplo en el se usa `filter()` en una lista en python. Este algoritmo filtra la lista `all_numbers` y retorna una nueva lista solo con los números impares:

```py
all_numbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

def my_function(numb):
    return numb % 2 == 0

odd_numbers = list(filter(my_function, all_numbers))
print(odd_numbers)
```

## 📝 Instrucciones:

1. Escribe el código necesario para obtener una lista `resulting_names` solo on los nombres que empiezan con la letra R.

2. Usa la función `filter()`.

## Resultado esperado:

```py
['Romario', 'Roosevelt']
```
