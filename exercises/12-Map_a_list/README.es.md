# `12` Map a list

```py
Python map()
```

La función `map()` aplica una función dada a cada elemento de un 'iterable' (ya sea lista, tupla, etc.) y devuelve una lista de resultados.

### La sintaxis de map() es:
 
```py
map(funcion, iterable, ...)
```

#### Parámetros de map():

- **función:** La función `map()` pasa cada elemento del iterable a esta función.

- **iterable:** iterable que será mapeado. Puedes pasarle más de un iterable a la función `map()`.

#### Valor devuelto por map():

La función `map()` aplica una función dada a cada elemento de un iterable y devuelve una lista de resultados.

El valor devuelto por `map()`, que es un map object, es pasado a funciones como `list()` (para crear una lista), `set()` (para crear un conjunto) y así.

## 📝 Instrucciones:

1. Usando la misma lógica, agrega el código necesario para convertir una lista de valores Celsius en Fahrenheit dentro de la función `map()`.

## Resultado esperado:

```py
Salida esperada en la consola:
[28.4, 93.2, 132.8, 14.0]
```
